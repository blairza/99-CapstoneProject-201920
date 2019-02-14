"""Zane Blair's Extra File"""
import time

def beep_move(robot,frequency,drop):
    k = 0
    robot.go(100,100)
    while True:
        if(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2):
          robot.stop()
          break
        robot.beep()
        time.sleep(frequency- drop*(k))
        k += 1

def spin(robot,direction,speed):
    """Figure out what the function is to find the object in the camera"""
    if(direction == 1):
        robot.drive_system.spin_clockwise_until_sees_object(speed,robot.sensor_system.camera.get_biggest_blob().get_area()-2)
    if (direction == -1):
        robot.drive_system.spin_counterclockwise_until_sees_object(speed,robot.sensor_system.camera.get_biggest_blob().get_area() - 2)