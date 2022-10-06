# robot_simulator
A differential drive robot simulator package in ROS2

## Install and Build the robot_simulation package

Prepare a folder to be used as catkin workspace by:
```console
mkdir -p <your_catkin_ws>/src
```
Navigate to this folder by:
```console
cd <your_catkin_ws>
```
Install the robot_simulator packages by running:
```console
cd src
git clone git@github.com:iamnawazahmed/robot_simulator.git
```
Go back to your workspace folder and build all packages by running:
```console
cd ../
colcon build
```

## Running the simulation

Setup/source your ROS2_PACKAGE_PATH by running:
```console
source install/setup.bash
```
Run robot_simulation by:
 ```console
ros2 launch robot_simulator worlds.launch.py
```
Open new terminal and setup your environment by running:
 ```console
source install/setup.bash
```
Control the robot via keyboard by:
 ```console
ros2 run robot_simulator teleop_twist_keyboard
```
