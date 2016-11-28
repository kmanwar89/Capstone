#! /usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
red = (255, 0, 0)
sense.set_rotation(180)
sense.low_light = True
sense.show_message("Hello world")
