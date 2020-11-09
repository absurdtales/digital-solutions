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
if temp > 20 and temp < 30 and pressure == 1013:
    bg = green
    sense.show_message("Temp Levels Normal: " + str(temp), scroll_speed)
else:
    bg = red
    ("WARNING TEMP LEVELS ABNORMAL: " + str(temp))

# This line of code tells the SenseHat to showcase the message and background colour 
sense.show_message(message, scroll_speed = 0.075, back_colour = bg)