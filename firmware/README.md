# Firmware

The firmware for this macro keyboard is built with [KMK](https://github.com/KMKfw/kmk_firmware).

Of course it is also possible to use [QMK](https://github.com/qmk/qmk_firmware), [ZMK](https://zmk.dev/), or your own firmware. Please make a [pull request](https://github.com/ruben-iteng/dreikon/pulls) if you made a compatible firmware!

## Installation

1. The first step is to install [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) on the RP2040. See [their tutorial](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython) on how to do this.

1. Download the latest KMK firmware [ZIP](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/main.zip), and extract it.

1. Copy over the `KMK` folder to the root of the `CircuitPy` drive.

1. Once that is done, copy over all the files in the [KMKfw](./KMKfw/) folder to the root of the `CircuitPy` drive.

1. If you want to change the behavior of the keys (e.g. macros), you can edit the [code.py](./KMKfw/code.py) file.

**TIP**: You can use [picotool](https://github.com/raspberrypi/picotool) to upload the CircuitPython firmware to the RP2040 and check specs of the board.

## Hardware pinout

| GPIO | Function |
|:----:|----------|
| 4    | Switch 0 |
| 17   | Switch 1 |
| 11   | Switch 2 |
| 7    | Config 0 |
| 6    | Config 1 |
| 5    | 5x WS2812B RGB LED string |
| 25   | RED status LED |

| LED | Function |
|:----:|----------|
| 0    | Switch 0 underglow |
| 1    | Switch 1 underglow |
| 2    | Switch 2 underglow |
| 3    | Front bar Left |
| 4    | Front bar Right |
