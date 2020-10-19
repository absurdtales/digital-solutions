from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

yellow = (255,255,0)
red = (255,0,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
magenta = (255,0,255)
black = (0,0,0)
white = (255,255,255)

sense.show_letter("M", black, back_colour=blue,)
sleep(.5)
sense.show_letter("A", black, back_colour=blue,)
sleep(.5)
sense.show_letter("R", black, back_colour=blue,)
sleep(.5)
sense.show_letter("I", black, back_colour=blue,)
sleep(.5)
sense.show_letter("O", black, back_colour=blue,)
sleep(.5)
sense.show_letter("7", black, back_colour=blue,)