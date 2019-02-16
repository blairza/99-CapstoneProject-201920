"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Trey Kline, Zane Blair, Ben Hawkins.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    inches_label = ttk.Label(frame, text="Inches")
    seconds_label = ttk.Label(frame, text="Seconds")
    seconds_entry = ttk.Entry(frame, width=8)
    go_straight_for_seconds_button = ttk.Button(frame, text="Make robot move for a number of seconds")
    inches_entry = ttk.Entry(frame, width=8)
    go_straight_for_inches_using_time_button = ttk.Button(frame, text="Make robot move a number of inches using time")
    go_straight_for_inches_using_encoder_button = ttk.Button(frame, text="Make robot move a number of inches using encoder")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    seconds_label.grid(row=6, column=0)
    seconds_entry.grid(row=8, column=0)
    go_straight_for_seconds_button.grid(row=8, column=2)
    inches_label.grid(row=9, column=1)
    inches_entry.grid(row=10, column=1)
    go_straight_for_inches_using_time_button.grid(row=11, column=0)
    go_straight_for_inches_using_encoder_button.grid(row=11, column=2)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    go_straight_for_seconds_button["command"] = lambda: handle_go_straight_for_seconds(seconds_entry, left_speed_entry,mqtt_sender)
    go_straight_for_inches_using_time_button["command"] = lambda: handle_go_straight_for_inches_using_time(inches_entry,left_speed_entry,mqtt_sender)
    go_straight_for_inches_using_encoder_button["command"] = lambda: handle_go_straight_for_inches_using_encoder(inches_entry,left_speed_entry, mqtt_sender)

    return frame

def get_proximity_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()

    frame_label = ttk.Label(frame, text='Proximity Sensor')
    forward_button = ttk.Button(frame, text='Go forward until distance is less than')
    forward_entry = ttk.Entry(frame, width=8)

    backward_button = ttk.Button(frame, text='Go backward until distance is greater than')
    backward_entry = ttk.Entry(frame, width=8)

    delta_button = ttk.Button(frame, text='Go until distance is within')
    delta_entry = ttk.Entry(frame, width=8)
    delta_distance_entry = ttk.Entry(frame, width=8)

    speed_label = ttk.Label(frame, text='Speed')
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, '100')

    frame_label.grid(row=0, column=1)
    forward_button.grid(row=1, column=0)
    forward_entry.grid(row=1, column=2)
    backward_button.grid(row=2, column=0)
    backward_entry.grid(row=2, column=2)
    delta_button.grid(row=3, column=0)
    delta_distance_entry.grid(row=3, column=1)
    delta_entry.grid(row=3, column=2)
    speed_label.grid(row=4, column=0)
    speed_entry.grid(row=4, column=1)


    forward_button["command"] = lambda: handle_go_forward_until_distance_is_less_than(forward_entry, speed_entry, mqtt_sender)
    backward_button["command"] = lambda : handle_go_backward_until_distance_is_greater_than(backward_entry, speed_entry, mqtt_sender)
    delta_button["command"] = lambda : handle_go_until_distance_is_within(delta_entry, delta_distance_entry, speed_entry, mqtt_sender)

    return frame

def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_sound_frame(window, mqtt_sender):
    """
    Makes a frame for the sound related robot functions
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """

    #makes the frame
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    #Constructs frame widgets
    beep_entry = ttk.Entry(frame, width=5)
    beep_button = ttk.Button(frame, text="Beep this many times")

    tone_entry_freq = ttk.Entry(frame, width=5)
    tone_label_freq = ttk.Label(frame, text="Choose Tone Frequency")
    tone_entry_length = ttk.Entry(frame, width=5)
    tone_label_length = ttk.Label(frame, text="Choose Tone Duration in Milliseconds")
    tone_button = ttk.Button(frame, text="Play a tone for this frequency and duration")

    speak_entry = ttk.Entry(frame)
    speak_button = ttk.Button(frame, text="Say this entry")

    #Grid these widgets
    beep_entry.grid(row=0, column=0)
    beep_button.grid(row=0, column=2)

    tone_entry_freq.grid(row=1, column=0)
    tone_label_freq.grid(row=1, column=2)

    tone_label_length.grid(row=2, column=2)
    tone_entry_length.grid(row=2, column=0)

    tone_button.grid(row=3, column=1)

    speak_entry.grid(row=4, column=0)
    speak_button.grid(row=4, column=2)

    #set button functions
    beep_button["command"] = lambda: handle_beep(beep_entry, mqtt_sender)
    tone_button["command"] = lambda: handle_tone(tone_entry_freq, tone_entry_length, mqtt_sender)
    speak_button["command"] = lambda: handle_speak(speak_entry, mqtt_sender)

    return frame

def get_color_frame(window,mqtt_sender):
    frame = ttk.Frame(window,padding=10,borderwidth =5, relief= "ridge")
    frame.grid()

    title = ttk.Label(frame,text="Color Sensor")
    speed_entry = ttk.Entry(frame,width=5)
    speed_label = ttk.Label(frame,text="Speed to move at")
    color_entry = ttk.Entry(frame,width=5)
    color_label = ttk.Label(frame,text = "Color to detect")
    intensity_entry = ttk.Entry(frame,width=5)
    intensity_label = ttk.Label(frame,text = "Intensity to check for")

    is_color_button = ttk.Button(frame,text="Move robot until it reaches entered color")
    is_not_color_button = ttk.Button(frame,text = "Move robot until it is off of entered color")
    greater_than_button = ttk.Button(frame,text="Move robot until color intensity is greater than entered intensity")
    less_than_button = ttk.Button(frame,text="Move robot until color intensity is less than entered intensity")

    title.grid(row=0,column=1)
    speed_label.grid(row=1,column=0)
    speed_entry.grid(row=2,column=0)
    color_label.grid(row=1,column=1)
    color_entry.grid(row=2,column=1)
    intensity_label.grid(row=1,column=2)
    intensity_entry.grid(row=2,column=2)

    is_color_button.grid(row=3,column=1)
    is_not_color_button.grid(row=4,column=1)
    greater_than_button.grid(row=5,column=1)
    less_than_button.grid(row=6,column=1)

    is_color_button["command"] = lambda: handle_is_color(speed_entry,color_entry,mqtt_sender)
    is_not_color_button["command"] = lambda: handle_is_not_color(speed_entry,color_entry,mqtt_sender)
    greater_than_button["command"] = lambda: handle_greater_than(speed_entry,intensity_entry,mqtt_sender)
    less_than_button["command"] = lambda: handle_less_than(speed_entry,intensity_entry,mqtt_sender)

    return frame


def get_camera_frame(window, mqtt_sender):
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
    frame_label = ttk.Label(frame, text="Camera")
    display_camera_button = ttk.Button(frame, text="Show the Camera's values for the blob in the console")
    rotate_clockwise_button = ttk.Button(frame, text="Rotate Clockwise and stop when it sees an object")
    rotate_countclockwise_button = ttk.Button(frame, text="Rotate Counter Clockwise and stop when it sees an object")
    area_entry = ttk.Entry(frame)
    area_label = ttk.Label(frame, text="The area of the object in order for the robot to stop spinning")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    display_camera_button.grid(row=1, column=1)
    rotate_clockwise_button.grid(row=3, column=0)
    rotate_countclockwise_button.grid(row=3, column=2)
    area_entry.grid(row=2, column=0)
    area_label.grid(row=2, column=1)

    # Set the Button callbacks:
    display_camera_button["command"] = lambda: handle_camera_display(mqtt_sender)
    rotate_countclockwise_button["command"] = lambda: handle_counterclockwise_camera(area_entry, mqtt_sender)
    rotate_clockwise_button["command"] = lambda: handle_clockwise_camera(area_entry, mqtt_sender)

    return frame



###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("Forward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("Backward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("backward", [left_entry_box.get(), right_entry_box.get()])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("Left", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("left", [left_entry_box.get(), right_entry_box.get()])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("Right", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("right", [left_entry_box.get(), right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Stop")
    mqtt_sender.send_message("stop")


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Raise Arm")
    mqtt_sender.send_message("raise_arm")


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Lower Arm")
    mqtt_sender.send_message("lower_arm")


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Calibrate The Arm")
    mqtt_sender.send_message("calibrate_arm")


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("Move arm to position", arm_position_entry.get())
    mqtt_sender.send_message("move_arm_to_position", [arm_position_entry.get()])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print("Stop quit cancel, guys quit")
    mqtt_sender.send_message("quit")


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print("Exit")
    handle_quit(mqtt_sender)
    exit()


def handle_go_straight_for_seconds(seconds,left,mqtt_sender):
    print("Moving for", seconds.get(), "seconds")
    mqtt_sender.send_message("go_straight_for_seconds",[seconds.get(),left.get()])


def handle_go_straight_for_inches_using_time(inches,left,mqtt_sender):
    print("Moving", inches.get(), "inches")
    mqtt_sender.send_message("go_straight_for_inches_using_time",[inches.get(),left.get()])


def handle_go_straight_for_inches_using_encoder(inches,left,mqtt_sender):
    print("Moving", inches.get(),"inches")
    mqtt_sender.send_message("go_straight_for_inches_using_encoder",[inches.get(),left.get()])


#########
# Handlers for Sound Frame
#########


def handle_beep(beep_entry, mqtt_sender):
    mqtt_sender.send_message("beep", [beep_entry.get()])


def handle_tone(freq_entry, length_entry, mqtt_sender):
    mqtt_sender.send_message("tone", [freq_entry.get(), length_entry.get()])


def handle_speak(speak_entry, mqtt_sender):
    mqtt_sender.send_message("speak", [speak_entry.get()])


########
# Handlers for Color Frame
########
def handle_is_color(speed_entry,color_entry,mqtt_sender):
    mqtt_sender.send_message("is_color",[speed_entry.get(),color_entry.get()])


def handle_is_not_color(speed_entry,color_entry,mqtt_sender):
    mqtt_sender.send_message("is_not_color",[speed_entry.get(),color_entry.get()])


def handle_greater_than(speed_entry,intensity_entry,mqtt_sender):
    mqtt_sender.send_message("greater",[speed_entry.get(),intensity_entry.get()])


def handle_less_than(speed_entry,intensity_entry, mqtt_sender):
    mqtt_sender.send_message("less",[speed_entry.get(), intensity_entry.get()])

###################3
#Handlers for Proximity Sensor Frame
####################


def handle_go_forward_until_distance_is_less_than(distance_entry, speed_entry, mqtt_sender):
    mqtt_sender.send_message('go_forward_until_distance_is_less_than', [distance_entry.get(), speed_entry.get()])


def handle_go_backward_until_distance_is_greater_than(distance_entry, speed_entry, mqtt_sender):
    mqtt_sender.send_message('go_backward_until_distance_is_greater_than', [distance_entry.get(), speed_entry.get()])


def handle_go_until_distance_is_within(delta_entry, distance_entry,  speed_entry, mqtt_sender):
    mqtt_sender.send_message('go_until_distance_is_within', [delta_entry.get(), distance_entry.get(), speed_entry.get()])

########
# Handles for camera functions
########


def handle_camera_display(mqtt_sender):
    print("handle camera display")
    mqtt_sender.send_message('display_camera', [])


def handle_counterclockwise_camera(area_entry, mqtt_sender):
    print("handle counterclockwise camera")
    mqtt_sender.send_message('counterclockwise_camera', [area_entry.get()])


def handle_clockwise_camera(area_entry, mqtt_sender):
    print("handle clockwise camera")
    mqtt_sender.send_message('clockwise_camera', [area_entry.get()])

