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

def spin(robot,direction,speed):
    """Figure out what the function is to find the object in the camera"""
    if(direction == 1):
        robot.drive_system.spin_clockwise_until_sees_object(speed,robot.sensor_system.camera.get_biggest_blob().get_area()-2)
    if (direction == -1):
        robot.drive_system.spin_counterclockwise_until_sees_object(speed,robot.sensor_system.camera.get_biggest_blob().get_area() - 2)

def move_to(robot,direction,speed):
    spin(robot,direction,speed)
    robot.drive_system.go_forward_until_distance_is_less_than(2,speed)

def pick_up(robot,direction,speed):
    move_to(robot,direction,speed)
    robot.arm_and_claw.raise_arm()