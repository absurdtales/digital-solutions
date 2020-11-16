# Initialising SenseHat
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Creating colour values for alert system
red = (255,0,0)
green = (0,255,0)

# Defining Temperature and Pressure values to utilize
temp = sense.get_temperature()
pressure = sense.get_pressure()

temp = round(temp,1)
pressure = round(pressure,1)

print("Temperature =", temp)
print("Pressure =", pressure)

# Creating the message to show on the SenseHat
message = "Temp: " + str(temp) + " Pressure: " + str(pressure)

# Average temperature on the ISS is around 24 degrees celcius, so I've given the normal levels a 10 degree leeway.
# Pressure on ISS is 101.3 kPa, anything other than this value could ruin equipment.
# Anything outside of these values would indicate the temperature sensor is malfunctioning on the ISS, and the pressure is wack.
if temp > 20 and temp < 50 and pressure == 1013:
    bg = green
    sense.show_message(f"Temp and Pressure Levels Normal: {temp}, {pressure}")
else:
    bg = red
    (f"WARNING TEMP AND PRESSURE LEVELS ABNORMAL: {temp}, {pressure}")



# This code will allow the screen to be turned off when pressing the joystick
while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            
            if event.direction == 'up':
                sense.clear()
            elif event.direction == 'down':
                sense.clear()
            elif event.direction == 'right':
                sense.clear()
            elif event.direction == 'left':
                sense.clear()