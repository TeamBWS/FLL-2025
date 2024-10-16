from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()
motor = Motor(Port.B, Direction.CLOCKWISE)
motor_2 = Motor(Port.D, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(motor, motor_2, 55, 128)


# The main program starts here.
drive_base.straight(250)
while not any(prime_hub.buttons.pressed()):
    wait(1)
motor.run_angle(500, 360)
