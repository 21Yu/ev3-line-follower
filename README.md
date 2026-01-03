# EV3 Line-Following Robot

This project is a LEGO EV3 robot programmed with Pybricks MicroPython that follows a colored line using PID control, detects obstacles with an ultrasonic sensor, and performs different actions depending on the detected color. 

---

## Demo

![Line Following](part1.gif)

![Obstacle Detection](part2.gif)

![PID Tuning](part3.gif)

---

## Features

- **PID-based line following** using the blue channel of the color sensor
- **Big-angle correction** when the robot loses the line
- **Obstacle detection** using an ultrasonic sensor
- **Color-based behavior** when an obstacle is detected:
  - Green detected → push forward and maneuver
  - Non-green (blue/other) → turn 180°
- Modular logic suitable for expansion or tuning

---

## Hardware Requirements

- LEGO EV3 Brick
- 2× Large Motors
  - Left Motor → Port A
  - Right Motor → Port D
- Color Sensor → Port S1
- Ultrasonic Sensor → Port S2

---

## Software Requirements

- Pybricks MicroPython
- EV3 firmware compatible with Pybricks

---

## Getting Started

1. Install Pybricks MicroPython on your EV3.
2. Connect motors and sensors according to the port assignments.
3. Upload the Python script to the EV3.
4. Place the robot on a blue line and start the program.

---

## How It Works

### 1. Line Detection

The robot uses the blue RGB value from the color sensor to follow a line.
A threshold (blueTher) defines the target line value.

```python
blueErr = blue - blueTher
```

### 2. PID Control

The motor speeds are adjusted using a PID controller:
- **P** – Current error
- **I** – Accumulated error over time
- **D** – Rate of error change

```python
uBlue = kpBlue * pBlue + kiBlue * iBlue + kdBlue * dBlue
```

### 3. Big-Angle Correction

If the blue value becomes too high, the robot assumes it lost the line and:
- Stops
- Rotates in place to search for it again

### 4. Obstacle Handling

When an object is detected within 100 mm:
- Robot stops
- Checks the green color value
- Executes a maneuver based on detected color

---

## Behavior Summary

| Condition | Action | 
|------|-----|
| Green line detected | PID line following |
| Line lost | Rotate to search |
| Obstacle + green | Push forward and maneuver |
| Obstacle + blue/other | Turn 180° |

---

## Tuning Parameters
You may need to adjust these values depending on lighting and surface:
```python
blueTher = 18

kpBlue = 35
kiBlue = 55
kdBlue = 65
```

---

## Future Improvements
- Dynamic PID tuning
- Multiple line color support
- Sound feedback instead of screen text
