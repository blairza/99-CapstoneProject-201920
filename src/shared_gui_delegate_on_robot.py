"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Zane Blair, Ben Hawkins, and Trey Kline.
  Winter term, 2018-2019.
"""

class Receiver(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot """
        self.robot = robot
        self.is_time_to_stop = False

    def forward(self, left_wheel_speed, right_wheel_speed):
        print('Got forward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        print('Got backward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))

    def left(self, left_wheel_speed, right_wheel_speed):
        print('Got left', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(-int(left_wheel_speed), int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        print('Got right', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), -int(right_wheel_speed))

    def stop(self):
        print('Got stop')
        self.robot.drive_system.stop()

    def raise_arm(self):
        print('Got raise arm')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('Got lower arm')
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print('Got calibrate arm')
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, arm_position_entry):
        print('Got move are to position')
        self.robot.arm_and_claw.move_arm_to_position(int(arm_position_entry))

    def quit(self):
        print('Got quit')
        self.is_time_to_stop = True

    def exit(self):
        print('Got exit')

    def go_straight_for_seconds(self, seconds, speed):
        print('Got go straight for seconds:', seconds)
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def go_straight_for_inches_using_time(self, inches, speed):
        print('Got go straight for inches using time', inches)
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        print('Got go straight for inches using encoder', )
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def beep(self, times):
        print('Got beep', times)
        for k in range(int(times)):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, freq, length):
        print('Got tone', length)
        self.robot.sound_system.tone_maker.play_tone(int(freq), int(length))

    def speak(self, string):
        print('Got speak',string)
        self.robot.sound_system.speech_maker.speak(string)

    def is_color(self,speed,color):
        print('Got color', color)
        self.robot.drive_system.go_straight_until_color_is(color,speed)

    def is_not_color(self,speed,color):
        print('Got color', color)
        self.robot.drive_system.go_straight_until_color_is_not(color,speed)

    def greater(self,speed,intensity):
        print('Got intensity', intensity)
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(intensity,speed)

    def less(self,speed,intensity):
        print('Got intensity', intensity)
        self.robot.drive_system.go_straight_until_intensity_is_less_than(intensity,speed)