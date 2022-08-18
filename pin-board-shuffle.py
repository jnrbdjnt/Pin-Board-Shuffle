import random

pin_keypad = list(range(10))

def disp_keypad() :
    print(pin_keypad[0], pin_keypad[1], pin_keypad[2])
    print(pin_keypad[3], pin_keypad[4], pin_keypad[5])
    print(pin_keypad[6], pin_keypad[7], pin_keypad[8])
    print(' ', pin_keypad[9])

random.shuffle(pin_keypad)
disp_keypad()
