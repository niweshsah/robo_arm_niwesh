# my_arm_controllers.yaml

robot_arm_controller:
  type: "position_controllers/JointTrajectoryController"
  joints: [joint_0, joint_1, joint_2, joint_3, joint_4]
  # Set the control parameters according to your needs
  gains:
    joint_0: {p: 100.0, i: 0.01, d: 10.0}
    joint_1: {p: 100.0, i: 0.01, d: 10.0}
    joint_2: {p: 100.0, i: 0.01, d: 10.0}
    joint_3: {p: 100.0, i: 0.01, d: 10.0}
    joint_4: {p: 100.0, i: 0.01, d: 10.0}
  # Optional parameters
  state_publish_rate: 50
  action_ns: /robot_arm_controller
  # Define the trajectory constraints
  constraints:
    goal_time: 0.5
    stopped_velocity_tolerance: 0.01
    imax: 1.0

joint_state_controller:
  type: "joint_state_controller/JointStateController"
  publish_rate: 50
