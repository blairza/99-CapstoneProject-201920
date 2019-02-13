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