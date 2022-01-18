cmake_minimum_required(VERSION 3.0.2)
project(leo_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
)

add_message_files(FILES
  Imu.msg
  WheelOdom.msg
  WheelStates.msg
)

generate_messages()

catkin_package(
  CATKIN_DEPENDS
    message_runtime
    std_msgs
)
