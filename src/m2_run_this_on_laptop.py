"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Trey Kline.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import shared_gui
import tkinter
from tkinter import ttk

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
    music_window = tkinter.Tk()
    music_window.title('Maestro Bot')



    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    music_frame = ttk.Frame(music_window, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
    music_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, sound_frame, color_frame, proximity_frame, camera_frame = get_shared_frames(main_frame, mqtt_sender)
    find_object = get_my_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    maestro_bot_frames = get_music_frames(music_window, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, sound_frame, color_frame, proximity_frame, camera_frame, find_object)
    maestro_bot_frames.grid(row=0, column=0)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()
    music_window.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_frame(main_frame, mqtt_sender)
    color_frame = shared_gui.get_color_frame(main_frame, mqtt_sender)
    proximity_frame = shared_gui.get_proximity_frame(main_frame, mqtt_sender)
    camera_frame = shared_gui.get_camera_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, sound_frame, color_frame, proximity_frame, camera_frame

def grid_frames(teleop_frame, arm_frame, control_frame, sound_frame, color_frame, proximity_frame, camera_frame, find_object):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    sound_frame.grid(row=3, column=0)
    color_frame.grid(row=4, column=0)
    proximity_frame.grid(row=5, column=0)
    camera_frame.grid(row=0, column=1)
    find_object.grid(row=1, column=1)

def get_my_frames(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Find Object and Make Tones")
    freq_lable = ttk.Label(frame, text='Starting Frequency')
    rate_lable = ttk.Label(frame, text='Rate of Increase')

    freq_entry = ttk.Entry(frame, width='8')
    rate_entry = ttk.Entry(frame, width='8')

    start_button=ttk.Button(frame, text='Find Using IR')
    clockwise_button=ttk.Button(frame, text='Spin clockwise and Find')
    counterclockwise_button = ttk.Button(frame, text='Spin counterclockwise and Find')

    frame_label.grid(row=0, column=0)
    freq_lable.grid(row=1, column=0)
    freq_entry.grid(row=1, column=1)
    rate_lable.grid(row=2, column=0)
    rate_entry.grid(row=2, column=1)
    start_button.grid(row=3, column=0)
    clockwise_button.grid(row=3, column=1)
    counterclockwise_button.grid(row=3, column=2)

    start_button['command'] = lambda : handle_find_object_ir(freq_entry, rate_entry, mqtt_sender)
    clockwise_button['command'] = lambda : handle_find_object_camera(freq_entry, rate_entry, 1, mqtt_sender)
    counterclockwise_button['command'] = lambda: handle_find_object_camera(freq_entry, rate_entry, 0, mqtt_sender)

    return frame

def get_music_frames(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()

    frame_lable = ttk.Label(frame, text='Maestro Bot')
    songs_lable = ttk.Label(frame, text='Play built in songs')
    tempo_lable = ttk.Label(frame, text='tempo')

    dropdown = ttk.Combobox(frame)
    dropdown['values'] = ('Sans Undertale', 'All Star', 'Mobamba')
    dance_button = ttk.Button(frame, text='Dance')
    compose_music = ttk.Button(frame, text='Compose Music')
    read_music = ttk.Button(frame, text='Read Music')
    dame_tu_cosita = ttk.Button(frame, text='Dame tu Cosita')

    bpm_dance_box = ttk.Entry(frame, width='8')
    tempo_box = ttk.Entry(frame, width='8')
    times_box = ttk.Entry(frame, width='8')
    times_dance_box = ttk.Entry(frame, width='8')

    frame_lable.grid(row=0, column=0)
    songs_lable.grid(row=1, column=0)
    dropdown.grid(row=1, column=1)
    times_box.grid(row=1, column=2)
    dance_button.grid(row=2, column=0)
    times_dance_box.grid(row=2, column=1)
    bpm_dance_box.grid(row=2, column=1)
    compose_music.grid(row=3, column=0)
    read_music.grid(row=4, column=0)
    tempo_lable.grid(row=4, column=1)
    tempo_box.grid(row=4, column=2)
    dame_tu_cosita.grid(row=5, column=0)

    dance_button['command'] = lambda : handle_dance(bpm_dance_box, times_dance_box, mqtt_sender)
    read_music['command'] = lambda : handle_read_music(tempo_box, mqtt_sender)
    compose_music['command']=lambda : handle_write_music(mqtt_sender)
    dame_tu_cosita['command'] = lambda : handle_dame_tu_cosita(mqtt_sender)

    return frame


def handle_play_prebuilt_music(song, times, mqtt_sender):
    print('Playing song', song, times.get(), 'times')
    mqtt_sender.send_message('play_prebuilt_music', [song, int(times.get())])

def handle_dance(tempo, times, mqtt_sender):
    print('Dancing at ', tempo, 'bpm', times, 'times')
    mqtt_sender.send_message('dance', [tempo.get()])

def handle_read_music(tempo, mqtt_sender):
    print('Reading music')
    mqtt_sender.send_message('read_music', [tempo.get()])

def handle_write_music(mqtt_sender):
    print('Writing Music')
    mqtt_sender.send_message('write_music', [])

def handle_dame_tu_cosita(mqtt_sender):
    print('Calling dame tu cosita at 3 AM')
    mqtt_sender.send_message('dame_tu_cosita', [])

def handle_find_object_ir(freq, rate, mqtt_sender):
    print('Finding object', freq.get(), rate.get())
    mqtt_sender.send_message('m2_find_object_ir', [int(freq.get()), int(rate.get())])

def handle_find_object_camera(freq, rate, clockwise, mqtt_sender):
    print('Spinning and the finding object', freq.get(), rate.get(), clockwise)
    mqtt_sender.send_message('m2_find_object_camera', [int(freq.get()), int(rate.get()), int(clockwise)])



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()