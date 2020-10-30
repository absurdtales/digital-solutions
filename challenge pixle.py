from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

y=4
x=4

white = (255,255,255)

sense.set_pixel(4,4,white)

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.action == 'pressed':
            if event.direction == 'up':
                sense.clear()
                y=y+1
                sense.set_pixel(4,4,white)
            elif event.direction == 'down':
                sense.clear()
                y=y-1
                sense.set_pixel(4,4,white)
            elif event.direction == 'right':
                sense.clear()
                x=x+1
                sense.set_pixel(4,4,white)
            elif event.direction == 'left':
                sense.clear()
                x=x-1
                sense.set_pixel(4,4,white)

