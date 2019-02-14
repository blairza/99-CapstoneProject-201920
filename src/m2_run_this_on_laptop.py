"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Trey Kline.
  Winter term, 2018-2019.
  NOTE TO ZANE AND BEN: If you edit my program you double homophobic
"""

import mqtt_remote_method_calls as com
import shared_gui
import tkinter
from tkinter import ttk
import m1_run_this_on_robot
m1_run_this_on_robot.

def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('BSSE 420 Bapstone Broject')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, sound_frame, color_frame, proximity_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)


    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_frame(main_frame, mqtt_sender)
    color_frame = shared_gui.get_color_frame(main_frame, mqtt_sender)
    proximity_frame = shared_gui.get_proximity_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, sound_frame, color_frame, proximity_frame

def grid_frames(teleop_frame, arm_frame, control_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)

def get_my_frames(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Find Object")
    freq_lable = ttk.Label(frame, text='Starting Frequency')
    rate_lable = ttk.Label(frame, text='Rate of Increase')

    freq_entry = ttk.Entry(frame, width='8')
    rate_entry = ttk.Entry(frame, width='8')

    start_button=ttk.Button(frame, text='Start')

    frame_label.grid(row=0, column=0)
    freq_lable.grid(row=1, column=0)
    freq_entry.grid(row=1, column=1)
    rate_lable.grid(row=2, column=0)
    rate_entry.grid(row=2, column=1)
    start_button.grid(row=3, column=0)

    start_button['command'] = lambda : handle_find_object_ir(freq_entry, rate_entry, mqtt_sender)

def handle_find_object_ir(freq, rate, mqtt_sender):
    print('Finding object', freq.get(), rate.get())
    mqtt_sender.send_message('find_object_ir', [self.robot, freq.get(), ])


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()