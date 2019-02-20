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
        if rosebot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1.4:
            break
        time.sleep(1/rate_of_change * (rosebot.sensor_system.ir_proximity_sensor.get_distance()) / 30)
        rosebot.led_system.right_led.turn_on()
        if rosebot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1.4:
            break
        time.sleep(1/rate_of_change * (rosebot.sensor_system.ir_proximity_sensor.get_distance()) / 30)
        rosebot.led_system.left_led.turn_off()
        if rosebot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1.4:
            break
        time.sleep(1/rate_of_change * (rosebot.sensor_system.ir_proximity_sensor.get_distance()) / 30)
        rosebot.led_system.turn_both_leds_off()
        if rosebot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1.4:
            break
        time.sleep(1/rate_of_change * (rosebot.sensor_system.ir_proximity_sensor.get_distance()) / 30)
        if rosebot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1.4:
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
        rosebot.drive_system.spin_clockwise_until_sees_object(speed, 50)
        m3_proximity_sensor_pick_up(rosebot, rateofchange, speed)

    if spin_dir == 1:
        rosebot.drive_system.spin_counterclockwise_until_sees_object(speed, 150)
        rosebot.drive_system.go(-40, 40)
        time.sleep(1.3)
        rosebot.drive_system.stop()
        m3_proximity_sensor_pick_up(rosebot, rateofchange, speed)


class m3_EmotionSystem(object):

    def __init__(self):
        self.emotions = (
            'Indifferent',
            'Depressed',
            'Happy',
            'Mad',
            'Confident',
            'Anxious',
            'Confused',
        )
        self.current_emotion = self.emotions(0)
        self.num_of_changes = 0

    def __repr__(self):
        return self.current_emotion

    def change_emotion(self, emotion_number):
        self.current_emotion = self.emotions(emotion_number)
        self.num_of_changes += 1


def m3_clockwise_until_sees_object(rosebot, speed, area):
    """

    :type rosebot: rb.RoseBot
    :param speed:
    :param area:
    :return:
    """
    rosebot.drive_system.left_motor.turn_on(speed)
    rosebot.drive_system.right_motor.turn_on(-1 * speed)
    timespent = 0
    while timespent < 1000:
        if rosebot.sensor_system.camera.get_biggest_blob().get_area() > area:
            rosebot.drive_system.stop()
            return True
        timespent += 1
    return False


def m3_counterclockwise_until_sees_object(rosebot, speed, area):
    """

    :type rosebot: rb.RoseBot
    :param speed:
    :param area:
    :return:
    """
    rosebot.drive_system.left_motor.turn_on(-1*speed)
    rosebot.drive_system.right_motor.turn_on(speed)
    timespent = 0
    while timespent < 1000:
        if rosebot.sensor_system.camera.get_biggest_blob().get_area() > area:
            rosebot.drive_system.stop()
            return True
        timespent += 1
    return False


def m3_emotion_camera_pickup(rosebot, spin_dir):
    """
    Spins counter clockwise if spin direction is 1, spins clockwise if 0


    :type rosebot: rb.RoseBot
    :param spin_dir:
    :return:
    """
    if rosebot.m3_emotion_system.current_emotion == 'Depressed':
        pass
    else:
        rosebot.m3_emotion_system.change_emotion(5)
        if spin_dir == 0:
            if m3_clockwise_until_sees_object(rosebot, 30, 50) is True:
                m3_proximity_sensor_pick_up(rosebot, 2, 30)
                rosebot.m3_emotion_system.change_emotion(2)
            else:
                rosebot.m3_emotion_system.change_emotion(6)
        if spin_dir == 1:
            if m3_counterclockwise_until_sees_object(rosebot, 30, 50) is True:
                m3_proximity_sensor_pick_up(rosebot, 2, 30)
                rosebot.m3_emotion_system.change_emotion(2)
            else:
                rosebot.m3_emotion_system.change_emotion(6)


def m3_change_emotion(rosebot, emotionnum):
    """

    :type rosebot: rb.RoseBot
    :param emotionnum:
    :return:
    """
    if emotionnum < 7:
        rosebot.m3_emotion_system.change_emotion(emotionnum)
    else:
        print("You picked a number which was too large")


def m3_emotion_by_color(rosebot, speed):
    """

    :type rosebot: rb.RoseBot
    :param speed:
    :return:
    """
    rosebot.drive_system.go_straight_until_color_is_not(0, speed)
    if rosebot.sensor_system.color_sensocar.get_color() < 8:
        rosebot.m3_emotion_system.change_emotion(rosebot.sensor_system.color_sensocar.get_color() -1)
