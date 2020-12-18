cmake_minimum_required(VERSION 3.0.2)

project(leo_description)

find_package(catkin REQUIRED)

catkin_package()

install(
  DIRECTORY
    launch
    models
    urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(test/xacro.test)
endif()