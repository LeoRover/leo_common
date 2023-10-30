^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package leo_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.3.0 (2023-10-30)
------------------
* Add mecanum wheels to description package (`#5 <https://github.com/LeoRover/leo_common/issues/5>`_)
* Contributors: Aleksander Szymański

2.2.0 (2022-08-24)
------------------

2.1.0 (2022-01-31)
------------------
* Add simulated imu sensor
* Increase wheel friction
* Update ODE properties for links

2.0.1 (2021-12-28)
------------------
* Add imu_frame link and imu_translation parameter

2.0.0 (2021-12-02)
------------------

1.2.2 (2021-06-04)
------------------
* Fix swapped FR and RR wheels
* Update author and maintainer info

1.2.1 (2020-12-18)
------------------
* Add footprint_link parameter to <leo/> macro

1.2.0 (2020-12-18)
------------------
* Add macros.xacro file which contains <leo/>, <leo_gazebo/> and <leo_sim/> xacro macros
* Add simple xacro test
* Change CMakeLists formatting style

1.1.0 (2020-10-09)
------------------
* Bump minimum cmake version to 3.0.2
* Update package manifest

1.0.1 (2020-10-06)
------------------

1.0.0 (2020-09-23)
------------------
* Added gazebo references
* Added camera_optical_frame link which uses camera coordinate convention
* Added launch files for publishing robot state
* Added low-poly outline models for collision geometry
* Added physical properties for all links and revolute joints
* Added joints for rockers and antenna
* Replaced meshes with more optimized ones

0.3.0 (2020-06-01)
------------------
* Moved the launch files and rviz configs to leo_viz package

0.2.0 (2020-02-12)
------------------
* exported new, more up-to-date part models in COLLADA format
* added rviz.launch file
* changed camera link name to `camera_frame`

0.1.0 (2019-10-02)
------------------
* add camera_link to urdf
* listen for real joint states in joint_states_publisher
* simplify description, use xacro, update launch file
* first try at exporting Leo Rover model to URDF
