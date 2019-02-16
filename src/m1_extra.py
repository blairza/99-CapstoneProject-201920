"""Zane Blair's Extra File"""
import time
import rosebot as rb

def beep_move(robot,frequency,drop):
    """:type robot : rb.RoseBot"""
    k = 0
    k_max = int(frequency/drop)
    robot.drive_system.go(25,25)
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        if(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1.5):
          robot.drive_system.stop()
          break
        if(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < distance):
            robot.sound_system.beeper.beep()
            if(k == k_max):
                k = k_max-1
            else:
                k += 1
            time.sleep(frequency - drop * (k))
    robot.arm_and_claw.raise_arm()

def spin(robot,direction,speed):
    """:type robot : rb.RoseBot"""
    robot.arm_and_claw.raise_arm()
    if(direction == 1):
        robot.drive_system.spin_clockwise_until_sees_object(speed,1500)
    if (direction == -1):
        robot.drive_system.spin_counterclockwise_until_sees_object(speed,1500)
    robot.arm_and_claw.lower_arm()

def move_to(robot,speed):
    """:type robot : rb.RoseBot"""
    robot.drive_system.go_forward_until_distance_is_less_than(2,speed)

def pick_up(robot):
    """:type robot : rb.RoseBot"""
    beep_move(robot,1,0.2)