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
            'Curious',
            'Confused',
        )
        self.current_emotion = self.emotions[0]
        self.num_of_changes = 0

    def change_emotion(self, emotion_number):
        self.current_emotion = self.emotions(emotion_number)
        self.num_of_changes += 1


def m3_clockwise_until_sees_object(rosebot, speed, area):
    """
    The same as the function in drive system, except it goes for a limited amount of time

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
    The same as the function in drive system, except it goes for a limited amount of time

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
    if rosebot.m3_emotion_system.current_emotion != 'Depressed':
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
    This is a callable function to change the emotion of the robot from an entry without crashing if the number is too
    large

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
    Goes until it sees any color and then converts that color's number into an emotion. Does not run if the robot is
    depressed

    :type rosebot: rb.RoseBot
    :param speed:
    :return:
    """
    if rosebot.m3_emotion_system.current_emotion == "depressed":
        pass
    else:
        rosebot.drive_system.go_straight_until_color_is_not(0, speed)
        if rosebot.sensor_system.color_sensocar.get_color() < 8:
            rosebot.m3_emotion_system.change_emotion(rosebot.sensor_system.color_sensocar.get_color() - 1)


def m3_heckle(rosebot):
    """
    Heckle the robot, making its emotion either indifferent, if it is happy or confident, or depressed, if it is not

    :type rosebot: rb.RoseBot
    :return:
    """
    if rosebot.m3_emotion_system.current_emotion == "Happy" or rosebot.m3_emotion_system.current_emotion == "Confident":
        rosebot.m3_emotion_system.change_emotion(0)
    else:
        rosebot.m3_emotion_system.change_emotion(1)


def m3_praise(rosebot):
    """
    Praise the robot, making its emotion either indifferent, if it is depreseed, or confident in any other case

    :type rosebot: rb.RoseBot
    :return:
    """
    if rosebot.m3_emotion_system.current_emotion == "Depressed":
        rosebot.m3_emotion_system.change_emotion(0)
    else:
        rosebot.m3_emotion_system.change_emotion(4)


def m3_emotion_find(rosebot, speed):
    """
    If depressed, does nothing, otherwise, it will become curious and will see if there is an object within 10 units
    if not, will become confused, move forward for 3 seconds, and then check again. Will become happy if there is something
    otherwise, no change

    :type rosebot: rb.RoseBot
    :param speed:
    :return:
    """
    if rosebot.m3_emotion_system.current_emotion != "Depressed":
        rosebot.m3_emotion_system.change_emotion(5)
        if rosebot.sensor_system.ir_proximity_sensor.get_distance() > 10:
            rosebot.m3_emotion_system.change_emotion(6)
            rosebot.drive_system.go(speed, speed)
            time.sleep(3)
            rosebot.drive_system.stop()
            if rosebot.sensor_system.ir_proximity_sensor.get_distance() < 10:
                rosebot.m3_emotion_system.change_emotion(2)
        else:
            rosebot.m3_emotion_system.change_emotion(2)
