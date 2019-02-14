"""
This file was written by Ben Hawkins for the Rose-Hulman CSSE120 Final Project, and includes code for extra functions
to run on the robot
"""

import rosebot as rb
import time


def m3_proximity_sensor_pick_up(rosebot):
    """
    :type rosebot: rb.RoseBot
    :return:
    """
    rosebot.drive_system.go_forward_until_distance_is_less_than(3, rosebot.drive_system.left_motor.get_speed())
    rosebot.arm_and_claw.raise_arm()


def m3_proximity_sensor_led_shift(rosebot, rate_of_change):
    """

    :param rosebot: rb.RoseBot
    :param rate_of_change: int
    :return:
    """
    while True:
        rosebot.led_system.only_left_on()
        time.sleep(rate_of_change*(rosebot.sensor_system.InfraredProximitySensor.get_distance())/30)
        rosebot.led_system.right_led.turn_on()
        time.sleep(rate_of_change * (rosebot.sensor_system.InfraredProximitySensor.get_distance()) / 30)
        rosebot.led_system.left_led.turn_off()
        time.sleep(rate_of_change * (rosebot.sensor_system.InfraredProximitySensor.get_distance()) / 30)
        rosebot.led_system.turn_both_leds_off()
        time.sleep(rate_of_change * (rosebot.sensor_system.InfraredProximitySensor.get_distance()) / 30)


