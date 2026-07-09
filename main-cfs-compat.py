# Copyright (c) 2026 Gabriel Baranello
# SPDX-License-Identifier: MIT

import asyncio
import json
from pathlib import Path

class LaneData:
    def __init__(self, config):
        self.server = config.get_server()

        self.db = self.server.lookup_component("database")
        self.klippy = self.server.lookup_component("klippy_apis")

        self.material_file = Path(
            "/usr/data/creality/userdata/box/material_box_info.json"
        )
        self.last_mtime = 0
        self.materials = {}

        self.server.register_event_handler(
            "server:ready",
            self._handle_ready
        )

    async def _handle_ready(self):
        self.server.get_event_loop().create_task(self.monitor())

    async def monitor(self):
        while True:
            await self.update_lane_data()
            await asyncio.sleep(0.3)

    async def update_lane_data(self):
        
        if not self.material_file.exists():
            return

        mtime = self.material_file.stat().st_mtime
        if mtime != self.last_mtime:
            self.last_mtime = mtime
            with open(self.material_file) as f:
                self.materials = json.load(f)
        lane_data = {}
        if "materialBoxInfo" not in self.materials:
            return
        for i, info in enumerate(self.materials["materialBoxInfo"]):
            info = self.materials["materialBoxInfo"][i]
            lane_data[f"lane{i+1}"] = {
                "lane": str(i),
                "material": info["type"],
                "color": convert_color(info["color"]),
                "bed_temp": info["bedTemp"],
                "nozzle_temp": info["hotendTemp"],
            }
        await self.db.insert_item("lane_data", "", lane_data)


def convert_color(color):

    color = color.lstrip("#")

    if len(color) == 7 and color[0] == "0":
        color = color[1:]

    if len(color) == 6:
        color += "FF"

    return color.upper()

def load_component(config):
    return LaneData(config)
