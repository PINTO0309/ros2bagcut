# ros2bagcut
A tool that simply cuts rosbag files within a specified start and end date and time.

```bash
pip install ros2bagcut
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
