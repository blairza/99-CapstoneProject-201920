#######
#Additional Functions
####################3
import rosebot
import ev3dev.ev3 as ev3
import time
import math


def find_object_ir(robot, starting_frequency, rate_of_increase):
    robot.drive_system.go(50, 50)
    frequency = starting_frequency
    while True:
        ave = 0
        for k in range(4):
            ave = ave + robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        ave = ave / 4

        frequency = frequency + (rate_of_increase/ave)
        robot.sound_system.tone_maker.play_tone(frequency, 500)
        print(ave)

        if ave <=5:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break


def find_object_camera(robot, starting_frequency, rate_of_increase, clockwise):
    if clockwise == 1:
       robot.sensor_system.Camera.spin_clockwise_until_sees_object()
    if clockwise == 0:
        robot.sensor_system.Camera.spin_counterclockwise_until_sees_object()

    robot.drive_system.go(50, 50)
    frequency = starting_frequency
    while True:
        ave = 0
        for k in range(4):
            ave = ave + robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        ave = ave / 4

        frequency = frequency + (rate_of_increase/ave)
        robot.sound_system.tone_maker.play_tone(frequency, 500)

        if ave <=5:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break


