# Creality CFS Fix – OrcaSlicer Doesn't Detect the CFS

If OrcaSlicer cannot detect your Creality CFS when using Moonraker/Fluidd, or it trows error "OrcaSlicer cannot connect to < printer name >. Check if the printer is turned on and connected to the network." this project restores compatibility without requiring any modifications to OrcaSlicer.

Unlike other solutions, this project does not require recompiling or patching OrcaSlicer. Everything runs on the printer through a lightweight Moonraker component.

## Symptoms

You may experience one or more of these issues:

- OrcaSlicer shows no CFS.
- No filament slots appear.
- Automatic filament synchronization does not work.
- The printer is connected, but the CFS is missing.
- OrcaSlicer behaves as if the printer had no multi-material system.

## The problem

Creality firmware exposes CFS information using a proprietary `box` object instead of the `lane_data` structure expected by OrcaSlicer's Moonraker integration.

Because of this mismatch, OrcaSlicer cannot recognize the installed CFS even though the printer reports it correctly.

## The solution

This Moonraker component acts as a compatibility bridge. It reads Creality's `box` object, converts it into the standard `lane_data` format expected by OrcaSlicer, and stores it in the Moonraker database.

As a result, OrcaSlicer detects the CFS normally without requiring any modifications or recompilation.

## Features

- No OrcaSlicer patch required
- No firmware modification
- Runs entirely inside Moonraker
- Converts Creality `box` → standard `lane_data`
- Automatic updates while the printer is running
- Compatible with Creality printers that expose the box Klipper object (K1, K1 Max, K1C, and potentially other CFS-enabled models).

## Requirements

- Rooted printer
- Moonraker
- Creality CFS

## Installation

1. Root your printer (for example using the guide below) and connect to it through SSH.

   https://www.youtube.com/watch?v=9YtvhT4Tx_E

2. Download the ZIP from **Code → Download ZIP**.

3. Extract it to a USB drive so that this README is located in the root of the drive.

4. Insert the USB drive into the printer.

5. Run:

```bash
cd /tmp/udisk/sda1/
```

If that directory does not exist, use:

```bash
cd /tmp/udisk/sda/
```

Then install:

```bash
chmod +x install.sh
./install.sh
```