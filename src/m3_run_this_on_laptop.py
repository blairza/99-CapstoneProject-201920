"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Ben Hawkins.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import shared_gui_delegate_on_robot as sgd


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()          #Just a sender
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('CSSE 120 Capstone Project Window')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5)
    main_frame.grid()


    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, sound_frame = get_shared_frames(main_frame, mqtt_sender)
    grid_frames(teleop_frame, arm_frame, control_frame, sound_frame)
    color_frame = shared_gui.get_color_frame(main_frame, mqtt_sender)
    camera_frame = shared_gui.get_camera_frame(main_frame, mqtt_sender)
    IR_frame = shared_gui.get_proximity_frame(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # Done: Implement and call get_my_frames(...)
    my_frame = m3_get_my_frame(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    color_frame.grid(row=0, column=1)
    camera_frame.grid(row=1, column=1)
    my_frame.grid(row=2, column=1)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    my_root = tkinter.Tk()
    my_root.title("Sprint 3 Ben personal Project")

    new_frame = ttk.Frame(my_root, padding=10, borderwidth=5)
    new_frame.grid()
    sprint3_frame = m3_get_sprint3_frame(new_frame, mqtt_sender)



    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, sound_frame


def grid_frames(teleop_frame, arm_frame, control_frame, sound_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    sound_frame.grid(row=3, column=0)


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
    sprint2_speed_entry = ttk.Entry(frame)
    sprint2_speed_label = ttk.Label(frame, text="The speed at which it moves towards the object")
    camera_find_clockbutton = ttk.Button(frame, text="Use the Camera to find and pickup an object by spinning clockwise")
    camera_find_countbutton = ttk.Button(frame, text="Use the Camera to find and pickup an objecy by spinning "
                                                     "counterclockwise")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    IR_pickup_button.grid(row=1, column=1)
    sprint2_speed_entry.grid(row=4, column=0)
    sprint2_speed_label.grid(row=4, column=1)
    led_rateofchange.grid(row=2, column=0)
    rateofchange_label.grid(row=2, column=1)
    camera_find_clockbutton.grid(row=3, column=0)
    camera_find_countbutton.grid(row=3, column=1)

    # Set the Button callbacks:
    IR_pickup_button["command"] = lambda: handle_IR_pickup(led_rateofchange.get(), sprint2_speed_entry.get(), mqtt_sender)
    camera_find_countbutton["command"] = lambda: handle_camera_pickup(led_rateofchange.get(), sprint2_speed_entry.get(),
                                                                      0, mqtt_sender)
    camera_find_clockbutton["command"] = lambda: handle_camera_pickup(led_rateofchange.get(), sprint2_speed_entry.get(),
                                                                      1, mqtt_sender)
    return frame


def m3_get_sprint3_frame(window, mqtt_sender):
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
    frame_label = ttk.Label(frame, text="Ben's sprint 3 frame")
    heckle_button = ttk.Button(frame, text="Heckle the Robot")
    praise_button = ttk.Button(frame, text="Praise the Robot")
    change_emotion_entry = ttk.Entry(frame)
    change_emotion_button = ttk.Button(frame, text="Put in a number to change the emotion to that number")
    sprint3_speed_entry = ttk.Entry(frame)
    sprint3_speed_label = ttk.Label(frame, text="The speed at which it moves towards the object")
    emotion_find_clockbutton = ttk.Button(frame, text="Use the Camera to find and pickup an object by spinning"
                                                      " clockwise")
    emotion_find_countbutton = ttk.Button(frame, text="Use the Camera to find and pickup an object by spinning "
                                                     "counterclockwise")
    emotion_by_color_button = ttk.Button(frame, text="Change the emotion by reading a color")
    emotion_ir_find_button = ttk.Button(frame, text="See if there is an object in front of the robot")
    check_emotion_button = ttk.Button(frame, text="List the current emotion in the console")


    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    heckle_button.grid(row=1, column=0)
    praise_button.grid(row=1, column=2)
    sprint3_speed_label.grid(row=2, column=2)
    sprint3_speed_entry.grid(row=2, column=0)
    change_emotion_entry.grid(row=3, column=0)
    change_emotion_button.grid(row=3, column=2)
    emotion_find_clockbutton.grid(row=4, column=0)
    emotion_find_countbutton.grid(row=4, column=2)
    emotion_by_color_button.grid(row=5, column=0)
    emotion_ir_find_button.grid(row=5, column=2)
    check_emotion_button.grid(row=5, column=1)

    # Set the Button callbacks:
    check_emotion_button["command"] = lambda: handle_check_emotion(mqtt_sender)
    heckle_button["command"] = lambda: handle_heckle(mqtt_sender)
    praise_button["command"] = lambda: handle_praise(mqtt_sender)
    change_emotion_button["command"] = lambda: handle_change_emotion(change_emotion_entry.get(), mqtt_sender)
    emotion_find_clockbutton["command"] = lambda: handle_find_spin(0, mqtt_sender)
    emotion_find_countbutton["command"] = lambda: handle_find_spin(1, mqtt_sender)
    emotion_by_color_button["command"] = lambda: handle_emotion_color(sprint3_speed_entry.get(), mqtt_sender)
    emotion_ir_find_button["command"] = lambda : handle_emotion_ir_find(sprint3_speed_entry.get(), mqtt_sender)

    return frame


def handle_IR_pickup(rateofchange, speed, mqtt_sender):
    print("Handle IR Pickup")
    mqtt_sender.send_message('m3_proximity_sensor_pickup', [rateofchange, speed])


def handle_camera_pickup(rateofchange, speed, clockwiseorcounterclockwise, mqtt_sender):
    print("Handle Camera find and pickup")
    mqtt_sender.send_message('m3_camera_pickup', [rateofchange, speed, clockwiseorcounterclockwise])


def handle_check_emotion(mqtt_sender):
    #window2 = ttk.Frame(padding=20)
    #window2.grid()

    mqtt_sender.send_message('m3_check_emotion', [])
    #emotionlabel = ttk.Label(window2, text="The current emotion is: \n {}".format(emotion))
    #emotionlabel.grid()


def handle_heckle(mqtt_sender):
    print("Handle Heckle")
    mqtt_sender.send_message('m3_heckle', [])


def handle_praise(mqtt_sender):
    print("Handle Praise")
    mqtt_sender.send_message('m3_praise', [])


def handle_change_emotion(emotion, mqtt_sender):
    print("Handle Change Emotion")
    mqtt_sender.send_message('m3_change_emotion', [emotion])


def handle_find_spin(spin_dir, mqtt_sender):
    print("Handle Either Emotion spin clockwise/counterclockwise", spin_dir)
    mqtt_sender.send_message('m3_emotion_camera', [spin_dir])


def handle_emotion_color(speed, mqtt_sender):
    print("Handle Emotion By Color")
    mqtt_sender.send_message('m3_emotion_color', [speed])


def handle_emotion_ir_find(speed, mqtt_sender):
    print("Handle Emotion IR Find")
    mqtt_sender.send_message('m3_emotion_ir', [speed])


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
