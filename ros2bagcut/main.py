#!/usr/bin/python

from argparse import ArgumentParser
import os
import shutil
import pytz
import rosbag2_py
from datetime import datetime, timezone, timedelta

def convert_to_unix_time_ns_with_timezone(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    second: int,
    timezone_str: str,
) -> int:
    """
    Convert a given date and time in a specified timezone to Unix time in nanoseconds,
    ignoring the minutes part of the timezone offset.
    """
    # Create a timezone object with the specified timezone string
    tz = pytz.timezone(timezone_str)
    # Create a datetime object with the given parameters
    dt = datetime(year, month, day, hour, minute, second)
    # Get the offset in hours for the specified timezone, ignoring minutes
    offset_hours = tz.utcoffset(dt).total_seconds() // 3600
    # Create a new timezone object with only hours offset
    tz_offset_hours = timezone(timedelta(hours=offset_hours))
    # Assign the new timezone to the datetime object
    dt = dt.replace(tzinfo=tz_offset_hours)
    # Convert the datetime to UTC and get Unix timestamp in nanoseconds
    dt_utc = dt.astimezone(timezone.utc)
    unix_time_ns = int(dt_utc.timestamp() * 1e9)  # Convert seconds to nanoseconds
    return unix_time_ns

def main():
    parser = ArgumentParser()
    parser.add_argument(
        '-i',
        '--input_bag_file',
        type=str,
        help='Input bag file name.',
    )
    parser.add_argument(
        '-o',
        '--output_bag_file',
        type=str,
        help='Output bag file name.',
    )
    parser.add_argument(
        '-st',
        '--starttime',
        type=int,
        nargs=6,
        help=\
            'Cut start time and date, minute, second. ' +
            'If not specified, start from the beginning. ' +
            'e.g. --starttime {year} {mont} {day} {hour} {minute} {second}',
    )
    parser.add_argument(
        '-et',
        '--endtime',
        type=int,
        nargs=6,
        help=\
            'Cut end time and date, minute, second. ' +
            'If unspecified, to the end. ' +
            'e.g. --endtime {year} {mont} {day} {hour} {minute} {second}',
    )
    parser.add_argument(
        '-tz',
        '--timezone',
        type=str,
        default='Asia/Tokyo',
        choices=pytz.all_timezones,
        help='Time zone string.',
    )
    args = parser.parse_args()

    # Set input and output bag file names
    input_bag_file = args.input_bag_file
    output_bag_file = args.output_bag_file
    start_time = args.starttime if args.starttime else None
    end_time = args.endtime if args.endtime else None
    timezone_str = args.timezone
    """
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
    """
    if os.path.exists(output_bag_file):
        os.remove(output_bag_file)

    output_bag_file_ext = os.path.splitext(os.path.basename(output_bag_file))[0]
    if os.path.exists(output_bag_file_ext):
        shutil.rmtree(output_bag_file_ext)

    # Set start and end times with Unix timestamps (nanoseconds)
    start_time_ns = -1
    if start_time is not None:
        start_time_ns = convert_to_unix_time_ns_with_timezone(*start_time, timezone_str=timezone_str)
    end_time_ns = -1
    if end_time is not None:
        end_time_ns = convert_to_unix_time_ns_with_timezone(*end_time, timezone_str=timezone_str)

    # Set Reader and Writer
    reader = rosbag2_py.SequentialReader()
    writer = rosbag2_py.SequentialWriter()

    # Open input bag file
    storage_options = rosbag2_py.StorageOptions(uri=input_bag_file, storage_id='sqlite3')
    converter_options = rosbag2_py.ConverterOptions('', '')
    reader.open(storage_options, converter_options)

    # Open output bag file
    output_storage_options = rosbag2_py.StorageOptions(uri=output_bag_file_ext, storage_id='sqlite3')
    writer.open(output_storage_options, converter_options)

    # Copy topic metadata
    topics_info = reader.get_all_topics_and_types()
    for topic_info in topics_info:
        writer.create_topic(topic_info)

    # Filter and write messages
    while reader.has_next():
        (topic, data, timestamp) = reader.read_next()

        if start_time_ns == -1 and timestamp <= end_time_ns:
            writer.write(topic, data, timestamp)
        elif start_time_ns <= timestamp and end_time_ns == -1:
            writer.write(topic, data, timestamp)
        elif start_time_ns <= timestamp <= end_time_ns:
            writer.write(topic, data, timestamp)

if __name__ == '__main__':
    main()