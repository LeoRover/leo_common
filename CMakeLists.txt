cmake_minimum_required(VERSION 2.8.3)

project(leo_description)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir launch models urdf rviz)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
