"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Zane Blair, Ben Hawkins, and Trey Kline.
  Winter term, 2018-2019.
"""
import m1_extra
import m2_extra
import m3_extra
import time

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
        self.robot.drive_system.go_straight_until_color_is(int(color),int(speed))

    def is_not_color(self,speed,color):
        print('Got color', color)
        self.robot.drive_system.go_straight_until_color_is_not(int(color),int(speed))

    def greater(self,speed,intensity):
        print('Got intensity', intensity)
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity),int(speed))

    def less(self,speed,intensity):
        print('Got intensity', intensity)
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity),int(speed))

    def go_forward_until_distance_is_less_than(self, inches, speed):
        print('Got Inches and Speed for Go forward until distance is less than', inches, speed)
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        print('Got Inches and Speed for Go backward until distance is greater than', inches, speed)
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))

    def go_until_distance_is_within(self, delta, inches, speed):
        print('Got Delta, Inches, and Speed for Go until distance is within', delta, inches, speed)
        self.robot.drive_system.go_until_distance_is_within(int(delta), int(inches), int(speed))

    def display_camera(self):
        print("Got Display Camera")
        self.robot.drive_system.display_camera_data()

    def counterclockwise_camera(self, area):
        print("Got spin counterclockwise")
        self.robot.drive_system.spin_counterclockwise_until_sees_object(self.robot.drive_system.left_motor.get_speed(),
                                                                        int(area))

    def clockwise_camera(self, area):
        print("Got spin counterclockwise")
        self.robot.drive_system.spin_clockwise_until_sees_object(self.robot.drive_system.left_motor.get_speed(),
                                                                 int(area))

    def m1_beep_move(self,beep_frequency,beep_drop):
        print("CSSE120 is fun")
        print(beep_frequency)
        print(beep_drop)
        time.sleep(1)
        print(self.robot)
        time.sleep(2)
        m1_extra.beep_move(self.robot,float(beep_frequency),float(beep_drop))

    def m1_spin(self,speed,direction):
        print("Got spin")
        m1_extra.spin(self.robot, int(direction), int(speed))

    def m1_move_to(self,speed,direction):
        print("Got move to")
        m1_extra.move_to(self.robot, int(direction), int(speed))

    def m1_pick_up(self,speed,direction):
        print("Got pick up")
        m1_extra.pick_up(self.robot, int(direction), int(speed))

    def m2_find_object_ir(self, freq, rate):
        print('Got find object ir')
        m2_extra.find_object_ir(self.robot, int(freq), int(rate))

    def m3_proximity_sensor_pickup(self, rateofchange, speed):
        print('Got m3 Proximity sensor pickup')
        m3_extra.m3_proximity_sensor_pick_up(self.robot, int(rateofchange), int(speed))

    #def m3_ir_ledflash(self, rateofchange):
    #    print("Got IR LED Flash, rate of change:", rateofchange)
    #   m3_extra.m3_proximity_sensor_led_shift(self, int(rateofchange))

    def m2_find_object_camera(self, freq, rate, clockwise):
        print('Got find object using camera')
        m2_extra.find_object_camera(freq, rate, clockwise)

    def m3_camera_pickup(self, rateofchange, speed, clockwiseorcounterclockwise):
        print("Got camera pickup", rateofchange, speed, clockwiseorcounterclockwise) 
        m3_extra.m3_camera_pickup(self.robot, rateofchange, speed, clockwiseorcounterclockwise)
