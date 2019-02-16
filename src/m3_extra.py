"""
This file was written by Ben Hawkins for the Rose-Hulman CSSE120 Final Project, and includes code for extra functions
to run on the robot
"""

import rosebot as rb
import time


def m3_proximity_sensor_pick_up(rosebot, rate_of_change, speed):
    """
    :type rosebot: rb.RoseBot
    :type rate_of_change: int
    :return:
    """
    rosebot.drive_system.go(speed, speed)
    while True:
        rosebot.led_system.only_left_on()
        time.sleep(1/rate_of_change * (rosebot.sensor_system.ir_proximity_sensor.get_distance()) / 30)
        rosebot.led_system.right_led.turn_on()
        time.sleep(1/rate_of_change * (rosebot.sensor_system.ir_proximity_sensor.get_distance()) / 30)
        rosebot.led_system.left_led.turn_off()
        time.sleep(1/rate_of_change * (rosebot.sensor_system.ir_proximity_sensor.get_distance()) / 30)
        rosebot.led_system.turn_both_leds_off()
        time.sleep(1/rate_of_change * (rosebot.sensor_system.ir_proximity_sensor.get_distance()) / 30)
        if rosebot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1.2:
            break
    rosebot.drive_system.stop()
    rosebot.arm_and_claw.raise_arm()


def m3_proximity_sensor_led_shift(rosebot, rate_of_change):
    """

    :type rosebot: rb.RoseBot
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


def m3_camera_pickup(rosebot, rateofchange, speed, spin_dir):
    """
    Spins counter clockwise if spin direction is 1, spins clockwise if 0


    :type rosebot: rb.RoseBot
    :param spin_dir:
    :return:
    """
    if spin_dir == 0:
        rosebot.drive_system.spin_clockwise_until_sees_object(speed, 200)
        m3_proximity_sensor_pick_up(rosebot, rateofchange, speed)

    if spin_dir == 1:
        rosebot.drive_system.spin_counterclockwise_until_sees_object(speed, 200)
        m3_proximity_sensor_pick_up(rosebot, rateofchange, speed)
