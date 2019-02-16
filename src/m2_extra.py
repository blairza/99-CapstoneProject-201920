#######
#Additional Functions
####################3
import rosebot
import ev3dev.ev3 as ev3
import time
import math


def find_object_ir(robot, starting_frequency, rate_of_increase):
    robot.drive_system.go(100, 100)
    frequency = starting_frequency
    while True:
        ave = 0
        for k in range(8):
            ave = ave + robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        ave = ave / 8

        frequency = frequency + (rate_of_increase/ave)
        robot.sound_system.tone_maker(frequency, 500)

        if ave <=3:
            robot.drive_system.stop()
            robot.ArmAndClaw.raise_arm()
            break


def find_object_camera(robot, starting_frequency, rate_of_increase, clockwise):
    if clockwise == True:
       robot.sensor_system.Camera.spin_clockwise_until_sees_object()
    if clockwise == False:
        robot.sensor_system.Camera.spin_counterclockwise_until_sees_object()

    robot.drive_system.go(100, 100)
    frequency = starting_frequency
    while True:
        ave = 0
        for k in range(8):
            ave = ave + robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        ave = ave / 8

        frequency = frequency + (rate_of_increase/ave)
        robot.sound_system.tone_maker(frequency, 500)

        if ave <=3:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break


