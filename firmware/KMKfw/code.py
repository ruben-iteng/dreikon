from dreikon import DREIKONKeyboard, DREIKONRGBLEDs, DREIKONStatusLED
from kmk.keys import KC
from kmk.modules.macros import Macros


rgb = DREIKONRGBLEDs()
statusLED = DREIKONStatusLED()
macros = Macros()

keyboard = DREIKONKeyboard()
keyboard.extensions.append(rgb)
keyboard.modules.append(macros)


# ------------------------------------------------------------
# Macros
# ------------------------------------------------------------
# Documentation: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
MACRO_1 = KC.MACRO(
    on_press="Ruben",
    on_hold=None,
    on_release=None,
    blocking=True,
)
MACRO_2 = KC.MACRO(
    on_press="Says",
    on_hold=None,
    on_release=None,
    blocking=True,
)
MACRO_3 = KC.MACRO(
    on_press="Hello",
    on_hold=None,
    on_release=None,
    blocking=True,
)
MACRO_4 = KC.MACRO(
    on_press="...",
    on_hold=None,
    on_release=None,
    blocking=True,
)


# ------------------------------------------------------------
# Keymap & layers
# ------------------------------------------------------------
# Documentation: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/layers.md
keyboard.keymap = [
    # Default layer (0)
    [
        MACRO_1,
        MACRO_2,
        MACRO_3,
        MACRO_4,
        KC.MO(1),
    ],
    # Layer 1 (1)
    # RGB LED settings
    [
        KC.RGB_MODE_KNIGHT,
        KC.RGB_MODE_BREATHE,
        KC.RGB_MODE_BREATHE_RAINBOW,
        KC.RGB_TOG,
        KC.TRNS,
    ],
]

if __name__ == "__main__":
    keyboard.go()
