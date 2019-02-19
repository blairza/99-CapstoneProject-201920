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

def trivia_list():
    color_list = ["One old wives’ tale claims that if a woman is buried wearing the color black, she’ll come back to haunt the family","Blue birds cannot see the color blue","Green was a sacred color to the Egyptians representing the hope and joy of spring","In Japan yellow represents courage",]
    #driving_list

def blue_danube():
    song = []

def special_moves(robot,num):
    if(num == 1):
        robot.drive_system.go(100,50)
    if(num == 2):
        robot.sound_system.tone_maker.play_tone_sequence(blue_danube.song())
    if(num == 3):
        pick_up(robot)
    if(num ==4):
        print("yellow")
#oof its yellow btw


def color_trivia(robot,color,speed):
    """:type robot : rb.RoseBot"""
    robot.drive_system.go_straight_until_color_is(color,speed)
    for k in range (1,8):
        if(robot.sensor_system.color_sensor.get_color() == k):
            robot.sound_system.speech_maker.speak("Fun fact")
            time.sleep(0.1)
            robot.sound_system.speech_maker.speak(trivia_list.color_list[k-1])
            special_moves(robot,k)