# This is only a test to ensure build is correct.

import sys

from pyautogui import click, moveTo

from movelib import say_hello_to

if __name__ == '__main__':
    print("Moving mouse and click application started")
    say_hello_to(int(sys.argv[1]), int(sys.argv[2]))
