import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# SW1 = D9, SW2 = D10, SW3 = D11
keyboard.matrix = KeysScanner(
    pins=[board.D9, board.D10, board.D11],
)

# What each key does: 1, 2, 3
keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3]
]

if __name__ == '__main__':
    keyboard.go()
