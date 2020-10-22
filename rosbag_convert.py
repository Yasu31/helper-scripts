#!/usr/bin/env python3
import sys
import os
import subprocess
"""
converts rosbag file to CSV.
$ ./rosbag_convert.py /path/to/rosbag.bag /joint_states /hoge ...
"""

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("provide rosbag file and rostopics as argument.")
        exit()
    rosbag_filename = sys.argv[1]
    # get filename with extension removed
    rosbag_dir = os.path.dirname(rosbag_filename)
    rosbag_id = os.path.splitext(os.path.basename(rosbag_filename))[0]
    log_dir = os.path.join(rosbag_dir, rosbag_id)

    topics = sys.argv[2:]
    print(f"reading rosbag file:\t{rosbag_filename}")
    print(f"converting rostopics:\t{topics}")
    print(f"outputting to directory:\t{log_dir}")

    try:
        os.mkdir(log_dir)
    except FileExistsError:
        pass
    for topic in topics:
        output_file = os.path.join(log_dir,  f"{topic.replace('/','-' )}.csv")
        print(f"writing to {output_file}...")
        with open(output_file, "w") as f:
            subprocess.run(["rostopic", "echo", topic, "-p",
                            "-b", rosbag_filename], stdout=f)
