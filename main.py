#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait


# Initialize the EV3 brick
ev3 = EV3Brick()

# Initialize the motors
leftM = Motor(Port.A)
rightM = Motor(Port.D)

# Initialize the sensors
ultrasoundS = UltrasonicSensor(Port.S2)
colorS = ColorSensor(Port.S1)

# Threshold for green color detection
blueTher = 18

# Initialize PID variables
lastBlueErr = 0
iBlue = 0

# PID constants for green line
kpBlue = 35
kiBlue = 55
kdBlue = 65


while True:
    # Read the RGB values from the color sensor
    red, green, blue = colorS.rgb()
    distance = ultrasoundS.distance()
    # Print the RGB values to the EV3 screen (for debugging)
    # ev3.screen.clear()
    # ev3.screen.print(red, ",", green, ",", blue)

    # Calculate the error for the green line
    blueErr = blue - blueTher
    
    # big angle correction
    if blue > 25:
        leftM.stop()
        rightM.stop()
        wait(200)

         # Rotate the robot to look for the line
        leftM.run_angle(-200, 60)  # Adjust the angle as necessary
        rightM.run_angle(200, 60)
        

    # Green line PID calculations
    pBlue = blueErr
    iBlue += blueErr * 0.005
    dBlue = (blueErr - lastBlueErr) / 0.005
    uBlue = kpBlue * pBlue + kiBlue * iBlue + kdBlue * dBlue

    # Calculate motor speeds
    leftSpeed = 150 - uBlue
    rightSpeed = 150 + uBlue

    # Set motor speeds
    leftM.run(leftSpeed)
    rightM.run(rightSpeed)

    # Update the previous error
    lastBlueErr = blueErr
    if distance < 100:
        leftM.stop()
        rightM.stop()
        wait(500)
        ev3.screen.print("beep!")
        wait(2000)
        ev3.screen.clear()
    # green line
        if green > 17:
            # push 10 cm
            leftM.run_time(200, 1000)
            rightM.run_time(200, 1000)
            
            leftM.run_time(300, 2000)

            leftM.run_time(-300, 2000)
            rightM.run_time(300, 700)
        # blue line
        else:
            # turn 180 degrees
            leftM.run_angle(400, 500)
            rightM.run_angle(-400, 420)


    # Wait for the next time step
    wait(5)