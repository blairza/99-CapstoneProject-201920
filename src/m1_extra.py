"""Zane Blair's Extra File"""
import time
import rosebot as rb

def beep_move(robot,frequency,drop):
    """:type robot : rb.RoseBot"""
    k = 0
    k_max = int(frequency/drop)
    robot.drive_system.go(25,25)
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        if(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1.5):
          robot.drive_system.stop()
          break
        if(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < distance):
            robot.sound_system.beeper.beep()
            if(k == k_max):
                k = k_max-1
            else:
                k += 1
            time.sleep(frequency - drop * (k))
    robot.arm_and_claw.raise_arm()

def spin(robot,direction,speed):
    """:type robot : rb.RoseBot"""
    robot.arm_and_claw.raise_arm()
    if(direction == 1):
        robot.drive_system.spin_clockwise_until_sees_object(speed,1500)
    if (direction == -1):
        robot.drive_system.spin_counterclockwise_until_sees_object(speed,1500)
    robot.arm_and_claw.lower_arm()

def move_to(robot,speed):
    """:type robot : rb.RoseBot"""
    robot.drive_system.go_forward_until_distance_is_less_than(2,speed)

def pick_up(robot):
    """:type robot : rb.RoseBot"""
    beep_move(robot,1,0.2)

########################
# This is the beginning of my Sprint 3 code
########################


def new_moon(robot):
    robot.sound_system.speech_maker.speak("I will now move in a circle to represent the new moon")
    robot.drive_system.go(100,25)
    time.sleep(4)
    robot.drive_system.stop()


def blue_danube():
    song = [(261.63,500,100),(329.63,500,100),(392,500,100),(392,500,1000),(739.99,500,100),(739.99,500,1000),(659.25,500,100),(659.25,500,1000),(261.63,500,100),(261.63,500,100),(329.63,500,100),(392,500,100),(392,500,1000),(739.99,500,100),(739.99,500,1000),(698.46,500,100),(698.46,500,1000),(293.66,500,100),(293.66,500,100),(349.23,500,100),(440,500,100),(440,2000,100),(369.99,500,100),(392,500,100),(659.25,2000,100),(523.25,500,100),(329.63,500,100),(329.63,1000,100),(293.66,500,100),(440,1000,100),(392,500,100),(261.63,750,100),(261.63,250,100),(261.63,500,100),(261.63,500)]
    return song


def praise_the_sun(robot):
    robot.sound_system.speech_maker.speak("Praise the sun")
    robot.arm_and_claw.raise_arm()
    robot.drive_system.spin_clockwise_until_sees_object()
    robot.sensor_system.camera.get_biggest_blob()


def destroy_object(robot):
    robot.sound_system.speech_maker.speak("Destroy object")
    robot.drive_system.go_forward_until_distance_is_less_than(3,25)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go(100,-100)
    time.sleep(2)
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()


def pick_up_and_move_it(robot):
    robot.sound_system.speech_maker.speak("Moving an object")
    robot.drive_system.spin_clockwise_until_sees_object()
    robot.drive_system.go_forward_until_distance_is_less_than(3,25)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go(25,-25)
    time.sleep(2)
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_time(10,50)


def haiku(robot):
    robot.sound_system.speech_maker.speak("I am a robot")
    robot.sound_system.speech_maker.speak("I speak this haiku for you")
    robot.sound_system.speech_maker.speak("Did you enjoy it")


def special_moves(robot,num):
    if(num == 1):
        new_moon(robot)
    if(num == 2):
       robot.sound_system.speech_maker.speak("I will now play Blue Danube")
       robot.sound_system.tone_maker.play_tone_sequence(blue_danube())
    if(num == 3):
        pick_up(robot)
    if(num ==4):
        praise_the_sun(robot)
    if(num==5):
        destroy_object(robot)
    if(num == 6):
        pick_up_and_move_it(robot)
    if(num == 7):
        haiku(robot)


def color_trivia(robot,color,speed):
    """:type robot : rb.RoseBot"""
    color_list = ["One old wives’ tale claims that if a woman is buried wearing the color black, she’ll come back to haunt the family","Blue birds cannot see the color blue","Green was a sacred color to the Egyptians representing the hope and joy of spring","In Japan yellow represents courage","The color red does not make bulls angry because they are colorblind","The sun is actually white but looks yellow because of refraction","Too much of the color brown can act as a depressant"]
    robot.drive_system.go_straight_until_color_is(color,speed)
    print(robot.sensor_system.color_sensocar.get_color())
    for k in range (1,8):
        if(robot.sensor_system.color_sensocar.get_color() == k):
            robot.sound_system.speech_maker.speak("Fun fact")
            time.sleep(0.1)
            robot.sound_system.speech_maker.speak(color_list[k-1])
            special_moves(robot,k)
