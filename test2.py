from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
hebel = Motor(Port.A)
zange = Motor(Port.E)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=128)
drive_base.settings(straight_speed=900, turn_rate=100)

#drive_base.straight(500, )

#drive_base.turn(180)

#drive_base.straight(-500)

#drive_base.turn(-180)

zange.run_target(100, -80)

drive_base.straight(390)

drive_base.turn(37)

drive_base.straight(15)

hebel.run_angle(100, 80)

drive_base.straight(20)

hebel.run_angle(100, 150)

drive_base.turn(37)