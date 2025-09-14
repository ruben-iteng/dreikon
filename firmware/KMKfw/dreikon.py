import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.RGB import RGB
from kmk.extensions.statusled import statusLED


class DREIKONStatusLED(statusLED):
    def __init__(self):
        super().__init__(led_pins=[board.GP25])


# GPIO to key mapping - each line is a new row.
_KEY_CFG = [
    board.GP4,  # Switch 0
    board.GP17,  # Switch 1
    board.GP11,  # Switch 2
    board.GP7,  # Config 0
    board.GP6,  # Config 1
]


# Keyboard implementation class
class DREIKONKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            value_when_pressed=False,
            # optional arguments with defaults:
            pull=True,
            interval=0.02,  # Matrix sampling interval in ms
            debounce_threshold=2,  # Number of samples needed to change state, values greater than 1 enable debouncing, None disables debouncing. Only applicable for CircuitPython >= 9.2.0
            max_events=64,
        )


class DREIKONRGBLEDs(RGB):
    def __init__(self):
        super().__init__(
            pixel_pin=board.GP5,
            num_pixels=5,
            rgb_order=(0, 1, 2),  # RGB
        )
