PK
     �=(Z�a-qE  E  	   Lauf_1.pyfrom pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()
rechts = Motor(Port.A, Direction.CLOCKWISE)
links = Motor(Port.B, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(links, rechts, 56, 130)
Motor_D = Motor(Port.D, Direction.CLOCKWISE)


#Korallenriff einsammeln
drive_base.settings(straight_speed=900)
drive_base.settings(900)
drive_base.straight(290)
Motor_D.run_angle(900, -1000)
drive_base.settings(900)
drive_base.straight(-290)
Motor_D.run_angle(900, 1000)

#einsammeln
while not Button.RIGHT in prime_hub.buttons.pressed():
    wait(1)
drive_base.settings(straight_speed=300)
drive_base.straight(450, Stop.NONE)
drive_base.curve(270, 90, Stop.NONE)
drive_base.straight(850, Stop.NONE)
drive_base.settings(straight_speed=150)
drive_base.turn(-10)
drive_base.straight(190)
Motor_D.run_angle(200, -900)
drive_base.straight(-100)
drive_base.turn(100)
drive_base.curve(150, -12, Stop.NONE)
drive_base.straight(575)
drive_base.turn(-40)
drive_base.settings(straight_speed=900)
drive_base.straight(-400)
drive_base.straight(430)


#Alles andere Einsammeln
while not Button.RIGHT in prime_hub.buttons.pressed():
    wait(1)
drive_base.settings(straight_speed=800)
drive_base.straight(-50)
drive_base.straight(450, Stop.NONE)
drive_base.curve(280, 80, Stop.NONE)
drive_base.straight(850)
drive_base.settings(straight_speed=150)
drive_base.turn(-10)
drive_base.straight(210)
Motor_D.run_angle(200, -900)
drive_base.straight(-120)
drive_base.turn(100)
drive_base.curve(150, -12, Stop.NONE)
drive_base.settings(straight_speed=500)
drive_base.straight(595)
drive_base.turn(-20)
drive_base.settings(straight_speed=900)
drive_base.straight(-430)
drive_base.curve(200, -20)
drive_base.straight(450)

#krill ausladen
while not Button.RIGHT in prime_hub.buttons.pressed():
    wait(1)
drive_base.settings(straight_speed=300)
drive_base.straight(700)
drive_base.turn(49)
drive_base.straight(250)
Motor_D.run_angle(100,-300)
Motor_D.run_angle(900,300)
drive_base.settings(straight_speed=900)
drive_base.straight(-205, Stop.NONE)
drive_base.turn(135, Stop.NONE)
drive_base.straight(400, Stop.NONE)
drive_base.curve(200, -20, Stop.NONE)
drive_base.straight(250)
# The main program starts here.
None.curve(100, 90)


drive_base.straight(-30)
drive_base.settings(200)
drive_base.straight(290)
Motor_D.run_angle(900, -1000)
drive_base.settings(100)
drive_base.straight(-290)
Motor_D.run_angle(900, 1000)


# Geschwindigkeit einstellen
drive_base.settings(straight_speed=900)
# Korallenzucht
drive_base.straight(680)
drive_base.turn(-90)
drive_base.straight(140)
drive_base.straight(-50)
# Haifischbecken
drive_base.turn(50)
drive_base.straight(200)
drive_base.straight(-200)
# 3. Aufgabe
drive_base.turn(110)
drive_base.straight(400)
drive_base.turn(-113)
drive_base.straight(190)
# Anker
drive_base.straight(-205)
drive_base.turn(110)
drive_base.straight(100)
drive_base.turn(-60)
drive_base.straight(110)
drive_base.turn(-130)
drive_base.straight(500)
drive_base.turn(-45)
drive_base.straight(600)

#Koralle erhängen
while not Button.RIGHT in prime_hub.buttons.pressed():
    wait(1)
drive_base.settings(straight_speed=400)
drive_base.straight(-100)
drive_base.straight(570)
Motor_C.run_angle(9000, 1500)
drive_base.curve(-100,90, Stop.NONE)
drive_base.curve(150,-90, Stop.NONE)
drive_base.straight(100, Stop.NONE)
drive_base.turn(180)

#Krake+Schatz
while not Button.RIGHT in prime_hub.buttons.pressed():
    wait(1)
drive_base.settings(straight_speed=860)
drive_base.straight(330, Stop.NONE)
drive_base.curve(200, 93)
drive_base.settings(straight_speed=155)
drive_base.straight(170)
drive_base.straight(-30)
drive_base.straight(-200)
drive_base.settings(straight_speed=900)
drive_base.turn(120)
drive_base.straight(400)PK
     �=(Z=,J�       awaitaufknopfdruck.pyfrom pybricks.hubs import PrimeHub
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
PK 
     �=(Z�a-qE  E  	                 Lauf_1.pyPK 
     �=(Z=,J�                 l  awaitaufknopfdruck.pyPK      z   �    