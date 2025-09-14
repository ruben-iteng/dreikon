import board
from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP4,
    midi=False,
    mouse=False,
    usb_id={"manufacturer": "KMK Keyboards", "product": "DREIKON"},
)
