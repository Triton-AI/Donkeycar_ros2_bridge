# Set Up
## Ros2 source
source /opt/ros/${ROS_DISTRO}/setup.bash
## Source donkey environment
conda activate donkey

## Create ROS2 workspace
mkdir -p ~/donkeycar_ws/src
cd ~/donkeycar_ws/src

## Git clone 
git clone https://github.com/Triton-AI/Donkeycar_ros2_bridge.git

## cd to src dir
cd ~/donkeycar_ws/src/Donkeycar_ros2_bridge/Donkeycar_ros2_bridge
donkey createcar --path . --template ros2bridge