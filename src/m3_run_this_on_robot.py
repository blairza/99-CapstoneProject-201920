"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Ben Hawkins.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as guid


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    FinalProject()


def FinalProject():
    robot = rosebot.RoseBot()
    delegate = guid.Receiver(robot)
    mqtt_delegate = com.MqttClient(delegate)
    mqtt_delegate.connect_to_pc()

    while True:
        time.sleep(.01)
        if delegate.is_time_to_stop:
            break



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()