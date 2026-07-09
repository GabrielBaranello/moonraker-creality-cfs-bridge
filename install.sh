#!/bin/sh
# SPDX-License-Identifier: MIT

cp main-cfs-compat.py \
    /usr/data/moonraker/moonraker/moonraker/components/cfs_compat.py

grep -q "^\[cfs_compat\]" /usr/data/printer_data/config/moonraker.conf || \
printf "\n[cfs_compat]\n" >> /usr/data/printer_data/config/moonraker.conf

echo
echo "La instalación finalizó."
echo
echo "Reinicie la impresora."
echo
echo "Después del reinicio ejecute:"
echo "curl http://localhost:7125/server/database/item?namespace=lane_data"
echo
echo "Se espera un JSON con:"
echo "{ lane1: ..., lane2: ..., lane3: ..., lane4: ... }"
echo
echo "Si aparece 'Namespace \"lane_data\" not found'"
echo "o la estructura es diferente,"
echo "copie la salida y publique una Discussion en:"
echo "https://github.com/GabrielBaranello/moonraker-creality-cfs-bridge/discussions"