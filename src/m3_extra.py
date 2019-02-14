"""
This file was written by Ben Hawkins for the Rose-Hulman CSSE120 Final Project, and includes code for extra functions
to run on the robot
"""

import rosebot as rb
import time
import tkinter
from tkinter import ttk


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

def m3_get_my_frame(window, mqtt_sender):
    """
        Constructs and returns a frame on the given window, where the frame has
        Button objects to run the robot's camera programs (via MQTT).
          :type  window:       ttk.Frame | ttk.Toplevel
          :type  mqtt_sender:  com.MqttClient
        """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Ben's frame")
    IR_pickup_button = ttk.Button(frame, text="Use the IR Detector to pick up an object")
    IR_ledflash_button = ttk.Button(frame, text="Turn the LEDS on the Lego Unit on/off based on proximity to an object")
    led_rateofchange = ttk.Entry(frame)
    rateofchange_label = ttk.Label(frame, text="Ratio of how fast you want the LEDs to flash on/off")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    IR_pickup_button.grid(row=1, column=1)
    IR_ledflash_button.grid(row=3, column=0)
    led_rateofchange.grid(row=2, column=0)
    rateofchange_label.grid(row=2, column=1)

    # Set the Button callbacks:
    IR_pickup_button["command"] = lambda: handle_IR_pickup(mqtt_sender)
    IR_ledflash_button["command"] = lambda: handle_ir_ledflash(led_rateofchange.get(), mqtt_sender)

    return frame


def handle_IR_pickup(mqtt_sender):
    print("Handle IR Pickup")
    mqtt_sender.send_message('m3_proximity_sensor_pickup', [])


def handle_ir_ledflash(rateofchange, mqtt_sender):
    print("Handle IR LED Flash")
    mqtt_sender.send_message('m3_ir_ledflash', [rateofchange])
