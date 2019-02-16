"""Zane Blair's Extra File"""
import time
import rosebot as rb

def beep_move(robot,frequency,drop):
    """:type robot : rb.RoseBot"""
    k = 0
    robot.drive_system.go(100,100)
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        if(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2):
          robot.drive_system.stop()
          break
        if(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < distance):
            robot.sound_system.beeper.beep()
            time.sleep(frequency- drop*(k))
            k += 1
    robot.arm_and_claw.raise_arm()

def spin(robot,direction,speed):
    """:type robot : rb.RoseBot"""
    if(direction == 1):
        robot.drive_system.spin_clockwise_until_sees_object(speed,4000)
    if (direction == -1):
        robot.drive_system.spin_counterclockwise_until_sees_object(speed,4000)

def move_to(robot,direction,speed):
    """:type robot : rb.RoseBot"""
    spin(robot,direction,speed)
    robot.drive_system.go_forward_until_distance_is_less_than(2,speed)

def pick_up(robot,direction,speed):
    """:type robot : rb.RoseBot"""
    move_to(robot,direction,speed)
    robot.arm_and_claw.raise_arm()