"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Zane Blair.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as sgd

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #run_test_arm()
    capstone()

def run_test_arm():
    robot = rosebot.RoseBot()
    #print('Arm Lowering')
    robot.arm_and_claw.lower_arm()
    print('Arm Lowered')
    #robot.arm_and_claw.calibrate_arm()
    #print('Arm Calibrated')
    """print('Arm Raising')
    robot.arm_and_claw.raise_arm()
    print('Arm Raised')"""
    #Raise arm is stuck on the button so it ain't finishing


def capstone():
    rhobert = rosebot.RoseBot()
    print("This is the Capstone project implementation")
    receiver = sgd.Receiver(rhobert)
    mqtt_receiver = com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()
    while True:
        time.sleep(0.01)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()