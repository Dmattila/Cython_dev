from pyautogui import moveTo, click

import cython

def say_hello_to(a: cython.int, b: cython.int):
    buttontype: cython.string = "right"
    moveTo(a, b)
    click(button=buttontype)