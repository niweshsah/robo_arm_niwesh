#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from pynput import keyboard

# Initialize ROS node
rospy.init_node('teleop_arm_joints', anonymous=True)

# Create publishers for each joint controller
joint_publishers = {
  '0': rospy.Publisher('/robot_arm_controller/command/joint_0', Float64, queue_size=10),
  '1': rospy.Publisher('/robot_arm_controller/command/joint_1', Float64, queue_size=10),
  '2': rospy.Publisher('/robot_arm_controller/command/joint_2', Float64, queue_size=10),
  '3': rospy.Publisher('/robot_arm_controller/command/joint_3', Float64, queue_size=10),
  '4': rospy.Publisher('/robot_arm_controller/command/joint_4', Float64, queue_size=10)
}

# Track the selected joint and its position
selected_joint = '0'
joint_positions = {
  '0': 0.0,
  '1': 0.0,
  '2': 0.0,
  '3': 0.0,
  '4': 0.0
}

def on_press(key):
  global selected_joint

  try:
    # Check if the key corresponds to a joint
    if key.char in joint_publishers:
      selected_joint = key.char
      rospy.loginfo(f"Selected joint {selected_joint}")

    # Increment or decrement the joint position with 'w' and 's'
    elif key.char == 'w':
      joint_positions[selected_joint] += 0.1
      rospy.loginfo(f"Moving joint {selected_joint} to position {joint_positions[selected_joint]}")
      joint_publishers[selected_joint].publish(joint_positions[selected_joint])

    elif key.char == 's':
      joint_positions[selected_joint] -= 0.1
      rospy.loginfo(f"Moving joint {selected_joint} to position {joint_positions[selected_joint]}")
      joint_publishers[selected_joint].publish(joint_positions[selected_joint])

  except AttributeError:
    pass

def on_release(key):
  # Stop listener on 'esc' key
  if key == keyboard.Key.esc:
    rospy.loginfo("Exiting teleoperation")
    return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
