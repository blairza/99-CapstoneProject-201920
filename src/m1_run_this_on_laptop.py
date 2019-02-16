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
    teleop, arm, control,sound,color, camera, proximity = get_shared_frames(frame,sender)

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
    speed_entry = ttk.Entry(frame_me,width=5)
    speed_label = ttk.Label(frame_me,text = "Speed from 0 to 100")
    direction = ttk.Entry(frame_me,width=5)
    direction_label = ttk.Label(frame_me,text = "Enter 1 for clockwise and -1  for counter clockwise")
    spin_button = ttk.Button(frame_me,text = "Make robot spin to look at objects")


    frame_label.grid(row=0,column=1)
    beep_drop.grid(row=2,column=0)
    beep_drop_label.grid(row=1,column=0)
    beep_frequency.grid(row=2,column=2)
    beep_freq_label.grid(row=1,column=2)
    beep_move_button.grid(row=3,column=1)
    speed_label.grid(row=1,column=5)
    speed_entry.grid(row=2,column=5)
    spin_button.grid(row=2,column=6)
    direction.grid(row=2,column=7)
    direction_label.grid(row=1,column=7)

    beep_move_button["command"] = lambda: handle_beep_move(beep_frequency,beep_drop,sender)
    spin_button["command"] = lambda: handle_spin(speed_entry,direction,sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop,arm,control,sound,color, camera,proximity)

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
    camera = shared_gui.get_camera_frame(main_frame,mqtt_sender)
    proximity = shared_gui.get_proximity_frame(main_frame,mqtt_sender)
    return teleop, arm, control,sound,color, camera, proximity


def grid_frames(teleop_frame, arm_frame, control_frame,sound_frame,color_frame,camera_frame,proximity_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=0, column=1)
    control_frame.grid(row=1, column=0)
    sound_frame.grid(row=1,column=1)
    color_frame.grid(row=4,column=0)
    camera_frame.grid(row=4,column=1)
    proximity_frame.grid(row=3,column=0)

def handle_beep_move(beep_frequency,beep_drop,mqtt_sender):
    print("Got beep frequency", beep_frequency)
    mqtt_sender.send_message("m1_beep_move", [beep_frequency,beep_drop])

def handle_spin(speed,direction,mqtt_sender):
    print("Got direction", direction)
    mqtt_sender.send_message("m1_spin",[speed,direction])
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()