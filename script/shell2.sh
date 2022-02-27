source /home/simulations/public_sim_ws/devel/setup.bash
roslaunch load_params load_params.launch
source /home/simulations/ros2_sims_ws/install/setup.bash
ros2 run ros1_bridge parameter_bridge __name:=parameter_bridge