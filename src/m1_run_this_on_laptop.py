"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zane Blair.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    sender = com.MqttClient()
    sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('Rhobert User Interface')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    frame = ttk.Frame(root, padding = 10, borderwidth = 5, relief = "groove")
    frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop, arm, control,sound,color = get_shared_frames(frame,sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # Currently Going: Implement and call get_my_frames(...)
    windher = tkinter.Tk()
    windher.title('Personal Frames')
    frame_me = ttk.Frame(windher,padding=10,borderwidth=5,relief = "groove")
    frame_me.grid()

    frame_label = ttk.Label(frame_me,text= "Beep and move towards objects")
    beep_frequency = ttk.Entry(frame_me,width=5)
    beep_freq_label = ttk.Label(frame_me,text="Frequence of beeps")
    beep_drop = ttk.Entry(frame_me,width=5)
    beep_drop_label = ttk.Label(frame_me,text="Increasing frequency number")
    beep_move_button = ttk.Button(frame_me,text="Make robot beep and move")

    frame_label.grid(row=0,column=1)
    beep_drop.grid(row=2,column=0)
    beep_drop_label.grid(row=1,column=0)
    beep_frequency.grid(row=2,column=2)
    beep_freq_label.grid(row=1,column=2)
    beep_move_button.grid(row=3,column=1)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop,arm,control,sound,color)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()
    windher.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control = shared_gui.get_control_frame(main_frame, mqtt_sender)
    sound = shared_gui.get_sound_frame(main_frame,mqtt_sender)
    color = shared_gui.get_color_frame(main_frame,mqtt_sender)
    return teleop, arm, control,sound,color


def grid_frames(teleop_frame, arm_frame, control_frame,sound_frame,color_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=0, column=1)
    control_frame.grid(row=1, column=0)
    sound_frame.grid(row=1,column=1)
    color_frame.grid(row=0,column=2)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()