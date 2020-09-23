^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package leo_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
