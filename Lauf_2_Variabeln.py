from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# Set up all devices.
prime_hub_2 = PrimeHub()
rechts = Motor(Port.A, Direction.CLOCKWISE)
links = Motor(Port.B, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(links, rechts, 56, 130)
Motor_D = Motor(Port.D, Direction.CLOCKWISE)
Motor_C = Motor(Port.C, Direction.CLOCKWISE)

# Initialize variables.
aktuelle_aufgabe = 1
los = False

def Matrix():
    prime_hub_2.display.off()
    prime_hub_2.display.number(aktuelle_aufgabe)

def Aufgabe_1():
    global aktuelle_aufgabe
    prime_hub_2.display.number(1)
    drive_base.settings(straight_speed=700)
    drive_base.settings(900)
    drive_base.straight(300)
    Motor_D.run_angle(900, -1000)
    drive_base.settings(900)
    drive_base.straight(-290)
    Motor_D.run_angle(900, 1000)
    aktuelle_aufgabe = 2
    wait(100)

def Aufgabe_2():
    global aktuelle_aufgabe
    prime_hub_2.display.number(2)
    drive_base.settings(straight_speed=300)
    drive_base.straight(450, Stop.NONE)
    drive_base.curve(290, 90, Stop.NONE)
    drive_base.straight(850, Stop.NONE)
    drive_base.settings(straight_speed=150)
    drive_base.turn(-10)
    drive_base.straight(200)
    Motor_D.run_angle(1000, -950)
    drive_base.settings(straight_speed=400)
    drive_base.straight(-140)
    drive_base.turn(75)
    drive_base.settings(straight_speed=900)
    drive_base.straight(550)
    drive_base.curve(150, -30)
    Motor_D.run_angle(900, 200)
    wait(1100)
    drive_base.settings(straight_speed=900)
    drive_base.straight(-500)
    drive_base.straight(500)
    aktuelle_aufgabe = 3
    wait(100)

def Aufgabe_3():
    global aktuelle_aufgabe
    prime_hub_2.display.number(3)
    #Walfütterung
    drive_base.settings(355)
    drive_base.straight(540, Stop.NONE)
    drive_base.settings(80)
    drive_base.curve(200, 43, Stop.NONE)
    drive_base.settings(320)
    drive_base.straight(235)
    Motor_D.run_angle(200, -300)
    Motor_D.run_angle(900, 300)
    drive_base.curve(-600, -40)
    #Sonar
    drive_base.turn(-88)
    drive_base.straight(190)
    drive_base.turn(45)
    #Anglerfisch
    drive_base.curve(-550, -45)
    drive_base.curve(-170, -40)
    drive_base.curve(-200, 48)
    drive_base.straight(140, Stop.NONE)
    drive_base.curve(40, 25)
    drive_base.settings(straight_speed=900)
    drive_base.straight(-420, Stop.NONE)
    drive_base.curve(-185, 85, Stop.NONE)
    drive_base.straight(-640)
    aktuelle_aufgabe = 4
    wait(100)

def Aufgabe_4():
    global aktuelle_aufgabe
    prime_hub_2.display.number(4)

    # Geschwindigkeit einstellen
    drive_base.settings(straight_speed=900)
    # Korallenzucht
    drive_base.straight(670)
    drive_base.turn(-90)
    drive_base.straight(140)
    drive_base.straight(-50)
    # Haifischbecken
    drive_base.turn(50)
    drive_base.straight(200)
    drive_base.straight(-200)
    # Korallen Aufzuchtstation
    drive_base.turn(110)
    drive_base.straight(400)
    drive_base.turn(-110)
    drive_base.straight(200)
    # Anker
    drive_base.straight(-205)
    drive_base.turn(110)
    drive_base.straight(90)
    drive_base.turn(-61)
    drive_base.straight(108)
    drive_base.turn(-130)
    drive_base.curve(200, -13)
    drive_base.straight(500, Stop.NONE)
    drive_base.curve(110, -45)
    drive_base.straight(600)
    aktuelle_aufgabe = 5
    wait(100)


def Aufgabe_5():
    global aktuelle_aufgabe
    prime_hub_2.display.number(5)
    #koralle erhängen
    drive_base.settings(straight_speed=400)
    drive_base.straight(570)
    Motor_C.run_angle(-9000, 1500)
    drive_base.curve(-100,90, Stop.NONE)
    drive_base.curve(150,-90, Stop.NONE)
    drive_base.straight(100, Stop.NONE)
    drive_base.turn(180)
    aktuelle_aufgabe = 6
    wait(100)

def Aufgabe_6():
    global aktuelle_aufgabe
    prime_hub_2.display.number(6)
    drive_base.settings(straight_speed=860)
    drive_base.straight(330, Stop.NONE)
    drive_base.curve(200, 93)
    drive_base.settings(straight_speed=70)
    drive_base.straight(140)
    drive_base.straight(-170)
    drive_base.settings(straight_speed=900)
    drive_base.turn(120)
    drive_base.straight(400)
    aktuelle_aufgabe = 7
    wait(100)


def Aufgabe_7():
    global aktuelle_aufgabe
    prime_hub_2.display.number(7)
    drive_base.settings(150)
    drive_base.curve(-200, -85)
    drive_base.settings(300)
    drive_base.straight(-240)
    drive_base.settings(150)
    drive_base.curve(-220, 53)
    drive_base.settings(300)
    drive_base.straight(100)
    drive_base.settings(straight_speed=50)
    drive_base.turn(28)
    drive_base.settings(300)
    drive_base.straight(-180)
    drive_base.settings(150)
    drive_base.curve(-200, 60, Stop.NONE)
    drive_base.settings(300)
    drive_base.straight(170)
    drive_base.turn(-10)
    drive_base.straight(-300)
    drive_base.turn(30)
    drive_base.curve(-180, -140)
    drive_base.settings(900)
    drive_base.straight(550)
    drive_base.straight(-50)
    wait(100)


def Start():
    global los
    los = True
    while los:
        if aktuelle_aufgabe == 1:
            Aufgabe_1()
        elif aktuelle_aufgabe == 2:
            Aufgabe_2()
        elif aktuelle_aufgabe == 3:
            Aufgabe_3()
        elif aktuelle_aufgabe == 4:
            Aufgabe_4()
        elif aktuelle_aufgabe == 5:
            Aufgabe_5()
        elif aktuelle_aufgabe == 6:
            Aufgabe_6()
        elif aktuelle_aufgabe == 7:
            Aufgabe_7()
        else:
            pass
        los = False
        prime_hub_2.system.set_stop_button(None)


# The main program starts here.
while True:
    prime_hub_2.system.set_stop_button(None)
    if Button.LEFT in prime_hub_2.buttons.pressed() and aktuelle_aufgabe > 1:
        aktuelle_aufgabe = aktuelle_aufgabe - 1
        wait(300)
    elif Button.RIGHT in prime_hub_2.buttons.pressed() and aktuelle_aufgabe < 8:
        aktuelle_aufgabe = aktuelle_aufgabe + 1
        wait(300)
    else:
        pass
    Matrix()
    if Button.CENTER in prime_hub_2.buttons.pressed():
        wait(500)
        prime_hub_2.system.set_stop_button(Button.CENTER)
        Start()
    else:
        pass