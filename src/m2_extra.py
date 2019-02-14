#######
#Additional Functions
####################3
import rosebot
import ev3dev.ev3 as ev3
import time
import math


def find_object_ir(robot, starting_frequency, rate_of_increase):
    robot.go(100, 100)
    frequency = starting_frequency
    while True:
        ave = 0
        for k in range(8):
            ave = ave + robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        ave = ave / 8

        frequency = frequency + (rate_of_increase/ave)
        robot.SoundSystem.ToneMaker(frequency, 500)

        if ave <=3:
            robot.stop
            robot.ArmAndClaw.raise_arm()
            break


