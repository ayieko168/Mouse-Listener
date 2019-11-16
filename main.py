#!/usr/bin/python3

from pynput.keyboard import Key, Controller as kb
from pynput.mouse import Controller as ms

from time import sleep

keyboard = kb()
mouse = ms()

while 1:

    print("The current pointer position is {0}".format(mouse.position))

    sleep(0.25)
