# moonrake-creality-cfs-bridge
This is a bridge via Moonraker to use Creality's CFS's (Creality Filament System) old protocol instead of the new one. This allows for compatibility with slicing software that has not yet been updated to support the new protocol.
## The problem
Creality's new firmware has introduced changes that break compatibility with the original CFS protocol. This has caused issues for slicing software to be able to communicate with the printer correctly. New firmware versions use a different protocol for the CFS, which can lead to errors when trying to sinc the CFS with a slicing software that hasn't been updated to support the new protocol.
## The solution
use a moonraker custom component to translate the new protocol to the old one, allowing slicing software to communicate with the printer correctly whitout it nowing about the new protocol.
## How to install
1. [Root your printer](https://www.youtube.com/watch?v=9YtvhT4Tx_E) and conect via ssh to it.
2. Download the .zip file of moonraker-creality-cfs-bridge from the green `<> code` button and extract it to a USB drive in a way that this document is in the root directory.
3. Plug the USB drive into your printer.
4. Run:
```bash
cd /tmp/udisk/sda1/
```

* If it says `bash: /tmp/udisk/sda1/: No such file or directory`
then run:
```bash
cd /tmp/udisk/sda/
```

* Run the install script:
```bash
chmod +x install.sh
./install.sh
```