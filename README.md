# ros2bagcut
A tool that simply cuts rosbag files within a specified start and end date and time.

## 1. Install ROS2
```bash
DISTRO=humble

sudo apt update && sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

sudo apt install software-properties-common
sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install -y ros-${DISTRO}-rosbag2
```
## 2. Install ros2bagcut
```bash
pip install ros2bagcut
```
## 3. Usage
```
ros2bagcut \
-i rosbag2_2024_01_12-09_37_34_0.db3 \
-o rosbag2_2024_01_12-09_37_34_0_cut.db3 \
-st 2024 1 12 18 37 55 \
-tz Asia/Tokyo
```
```
usage: ros2bagcut
[-h]
[-i INPUT_BAG_FILE]
[-o OUTPUT_BAG_FILE]
[-st STARTTIME STARTTIME STARTTIME STARTTIME STARTTIME STARTTIME]
[-et ENDTIME ENDTIME ENDTIME ENDTIME ENDTIME ENDTIME]
[-tz {
  Africa/Abidjan
  Africa/Accra
  Africa/Addis_Ababa
  Africa/Algiers
  Africa/Asmara
  ...
  America/Adak
  America/Anchorage
  America/Anguilla
  ...
  Asia/Aden
  Asia/Almaty
  Asia/Amman
  Asia/Anadyr
  Asia/Aqtau
  Asia/Tokyo
  ...
  Europe/Amsterdam
  Europe/Andorra
  Europe/Astrakhan
  Europe/Athens
  Europe/Belgrade
  ...
  Pacific/Apia
  Pacific/Auckland
  Pacific/Bougainville
  ...
}]

options:
  -h, --help
    show this help message and exit
  -i INPUT_BAG_FILE, --input_bag_file INPUT_BAG_FILE
    Input bag file name.
  -o OUTPUT_BAG_FILE, --output_bag_file OUTPUT_BAG_FILE
    Output bag file name.
  -st STARTTIME STARTTIME STARTTIME STARTTIME STARTTIME STARTTIME, \
      --starttime STARTTIME STARTTIME STARTTIME STARTTIME STARTTIME STARTTIME
    Cut start time and date, minute, second.
    If not specified, start from the beginning.
    e.g. --starttime {year} {mont} {day} {hour} {minute} {second}
  -et ENDTIME ENDTIME ENDTIME ENDTIME ENDTIME ENDTIME, \
      --endtime ENDTIME ENDTIME ENDTIME ENDTIME ENDTIME ENDTIME
    Cut end time and date, minute, second.
    If unspecified, to the end.
    e.g. --endtime {year} {mont} {day} {hour} {minute} {second}
  -tz {...}, --timezone {...}
    Time zone string.
```
