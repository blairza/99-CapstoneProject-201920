"""
This file was written by Ben Hawkins for the Rose-Hulman CSSE120 Final Project, and includes code for extra functions
to run on the robot
"""

import rosebot as rb


def proximity_sensor_pick_up(rosebot, speed):
    """
    :type rosebot: rb.RoseBot
    :param speed:  int
    :return:
    """
    rosebot.drive_system.go_forward_until_distance_is_less_than(3, speed)
    rosebot.arm_and_claw.raise_arm()


def proximity_sensor_led_shift(rosebot):
    """

    :param rosebot: rb.RoseBot
    :return:
    """
    rosebot.led_system


