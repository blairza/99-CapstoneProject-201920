#######
#Additional Functions
####################3
import rosebot
import ev3dev.ev3 as ev3
import time
import math
import random
from PIL import Image



def find_object_ir(robot, starting_frequency, rate_of_increase):
    #Takes in a rosebot, starting frequency(int) and rate of increase(int)
    #Makes the robot find an object and as it gets closer the frequency of the beep increases
    robot.drive_system.go(50, 50)
    frequency = starting_frequency
    while True:
        ave = 0
        for k in range(4):
            time.sleep(0.05)
            ave = ave + robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        ave = ave / 4

        frequency = frequency + (rate_of_increase/ave)
        robot.sound_system.tone_maker.play_tone(frequency, 500)
        print(ave)

        if ave <=5:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break


def find_object_camera(robot, starting_frequency, rate_of_increase, clockwise):
    #Takes in a rosebot, starting frequency, rate of increase, and a number either 0 or 1.
    #If clockwise is 1 then the robot will rotate clockwise until it sees and ohject, then go towards it. If
    #clockwise is 0, it will spin counterclockwise and go find the object
    robot.arm_and_claw.raise_arm()
    if clockwise == 1:
       robot.drive_system.spin_clockwise_until_sees_object(25, 700)
    if clockwise == 0:
        robot.drive_system.spin_counterclockwise_until_sees_object(25, 700)
    robot.arm_and_claw.lower_arm()

    robot.drive_system.go(50, 50)
    frequency = starting_frequency
    while True:
        ave = 0
        for k in range(4):
            ave = ave + robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        ave = ave / 4

        frequency = frequency + (rate_of_increase/ave)
        robot.sound_system.tone_maker.play_tone(frequency, 500)

        if ave <=5:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break






def write_music(robot):
    #Takes in a rosebot. Uses the camera to detect a color. If more of SIG1s color is seenm it will randomly choose notes
    #in a minor key to play. If more of the other color is seen, it will do the same for a major key.
    key = 0
    bpm = 100
    robot.sensor_system.camera.set_signature('SIG2')
    happy_color = robot.sensor_system.camera.get_biggest_blob().get_area()
    robot.sensor_system.camera.set_signature('SIG1')
    sad_color = robot.sensor_system.camera.get_biggest_blob().get_area()

    if happy_color >= sad_color:
        key = 1
        bpm = 180

    scale = get_scale(key)
    notes = [scale[0]]
    lengths = [1]

    for k in range(15):
        note = 0
        number = random.randint(1, 10)
        interval = intervals(number)
        note = note + interval
        if note > 7:
            note = note - 8
        if note < 0:
            note = note + 8
        notes.append(scale[note])
        lengths.append(random.randint(1, 5))

    play_music(robot, notes, lengths, bpm)


def get_scale(key):
    #Takes in an int either 1 or 0.
    #If it is 1, returns a tuple containing the notes of the major scale and if it is 0 returns the minor scale
    major_scale = (  'C4',
                     'D4',
                     'E4',
                     'F4',
                     'G4',
                     'A5',
                     'B5',
                     'C5',
                     )

    minor_scale = (  'C4',
                     'D4',
                     'DS4',
                     'F4',
                     'G4',
                     'GS5',
                     'AS5',
                     'C5',
                     )
    if key == 1:
        return major_scale

    if key ==0:
        return minor_scale


def intervals(int):
    #Takes in an int 1-10.
    #Returns the coresponding interval value

    interval={1:1,
              2:2,
              3:3,
              4:4,
              5:5,
              6:-1,
              7:-2,
              8:-3,
              9:-4,
              10:-5
    }
    return interval[int]

def read_music(robot, tempo):
    #Takes in a rosebot and int, tempo.
    #Uses the color sensor to read a color every time the color changes.
    #Plays notes based on the color
    colors = []
    notes = []
    lengths = []
    robot.drive_system.go(50, 50)
    while True:
        current_color = robot.sensor_system.color_sensocar.get_color()
        colors.append(current_color)
        while True:
            print(robot.sensor_system.color_sensocar.get_color())
            if robot.sensor_system.color_sensocar.get_color() != current_color:
                break
            elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<=5:
                break

        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<=5:
            robot.drive_system.stop()
            break
    for k in range(len(colors)):
        notes.append(color_to_note(colors[k]))
        lengths.append(1)
    play_music(robot, notes, lengths, tempo)


def color_to_note(color):
    #Takes in an int representing a color from the sensor
    #Returns the corresponding note
    color_matrix = {1: 'C4',
                    2: 'D4',
                    3: 'E4',
                    4: 'F4',
                    5: 'G4',
                    6: 'A5',
                    7: 'B5',
                    0: 'C5',
                    }
    return color_matrix[color]


def dance(robot, bpm, times):
    #Takes in a robot a bpm int and a times int.
    # The robot will shake it's booty at the bpm for however many times that times is.
    beat = 60/bpm
    for k in range(times):
        robot.drive_system.go(100, -100)
        time.sleep(beat)
        robot.drive_system.stop()
        robot.drive_system.go(-100, 100)
        time.sleep(beat)
        robot.drive_system.stop()
        robot.drive_system.go(100, 100)
        time.sleep(beat)
        robot.drive_system.stop()
        robot.drive_system.go(-100, -100)
        robot.drive_system.stop()



def play_prebuilt_music(robot, song, times):
    #Takes in a rosebot, song (int 0-2), and times (int)
    #Plays a song on the rosebot and uses the song variable to select a song.

    more_bamba = [('C4', 'C4', 'F4', 'FS4', 'C4', 'C4', 'C4', 'F4'), (0.5, 1, 8, 3, 2, 1, 1, 8)]
    all_star = [('B4', 'G4', 'G4', 'E4', 'G4', 'G4', 'G4', 'E4', 'G4', 'G4', 'G4', 'B4'), (1, 2, 0.5, 0.5, 1, 2, 0.5, 0.5, 1, 2, 2, 1)]
    sans_undertale = [('D4', 'D4', 'D5', 'A4', 'GS4', 'G4', 'F4', 'D4', 'F4', 'G4', 'C4', 'C4', 'D5', 'A4', 'GS4', 'G4', 'F4', 'D4', 'F4', 'G4', 'B3', 'B3', 'D5', 'A4', 'GS4', 'G4', 'F4', 'D4', 'F4', 'G4', 'AS3', 'AS3', 'D5', 'A4', 'GS4', 'G4', 'F4', 'D4', 'F4', 'G4'), (0.25, 0.25, 0.5, 0.375, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.375, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25,0.25, 0.25, 0.5, 0.375, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25,0.25, 0.25, 0.5, 0.375, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25)]
    if song == 0:
        for k in range(times):
            play_music(robot, sans_undertale[0], sans_undertale[1], 240)

    if song == 1:
        for k in range(times):
            play_music(robot, all_star[0], all_star[1], 200)

    if song == 2:
        for k in range(times):
            play_music(robot, more_bamba[0], more_bamba[1], 180)


def play_music(robot, notes, lengths, tempo):
    tick = (60 / tempo)*1000
    print(len(notes))
    print(len(lengths))
    for k in range(len(notes)):
        robot.sound_system.tone_maker.play_tone(note_finder(notes[k]), tick*lengths[k]).wait()
    return


def note_finder(note):
    note_matrix = {
        'B0':31,
        'C1':33,
        'CS1': 35,
        'D1': 37,
        'DS1': 39,
        'E1':  41,
        'F1':  44,
        'FS1': 46,
        'G1':  49,
        'GS1': 52,
        'A1':  55,
        'AS1': 58,
        'B1':  62,
        'C2':  65,
        'CS2': 69,
        'D2':  73,
        'DS2': 78,
        'E2':  82,
        'F2':  87,
        'FS2': 93,
        'G2':  98,
        'GS2': 104,
        'A2':  110,
        'AS2': 117,
        'B2':  123,
        'C3':  131,
        'CS3': 139,
        'D3':  147,
        'DS3': 156,
        'E3':  165,
        'F3':  175,
        'FS3': 185,
        'G3':  196,
        'GS3': 208,
        'A3':  220,
        'AS3': 233,
        'B3':  247,
        'C4':  262,
        'CS4': 277,
        'D4':  294,
        'DS4': 311,
        'E4': 330,
        'F4':  349,
        'FS4': 370,
        'G4':  392,
        'GS4': 415,
        'A4':  440,
        'AS4': 466,
        'B4':  494,
        'C5': 523,
        'CS5': 554,
        'D5':  587,
        'DS5': 622,
        'E5':  659,
        'F5':  698,
        'FS5': 740,
        'G5':  784,
        'GS5': 831,
        'A5':  880,
        'AS5': 932,
        'B5':  988,
        'C6':  1047,
        'CS6': 1109,
        'D6':  1175,
        'DS6': 1245,
        'E6':  1319,
        'F6':  1397,
        'FS6': 1480,
        'G6':  1568,
        'GS6': 1661,
        'A6':  1760,
        'AS6': 1865,
        'B6':  1976,
        'C7':  2093,
        'CS7': 2217,
        'D7':  2349,
        'DS7': 2489,
        'E7':  2637,
        'F7':  2794,
        'FS7': 2960,
        'G7':  3136,
        'GS7': 3322,
        'A7':  3520,
        'AS7': 3729,
        'B7':  3951,
        'C8':  4186,
        'CS8': 4435,
        'D8':  4699,
        'DS8': 4978,
    }
    return note_matrix[note]


