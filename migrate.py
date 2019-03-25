import os
import glob
from subprocess import call
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="bag migration script")
    parser.add_argument("--in_root", type=str, default="")
    parser.add_argument("--out_root", type=str, default="")
    parser.add_argument("--bmr", type=str, default="")

    args = parser.parse_args()
    bmr_file = args.bmr
    in_root = args.in_root
    out_root = args.out_root

    dirs = []

    for dir in os.listdir(in_root):
        if os.path.isdir(os.path.join(in_root, dir)):
            dirs.append(dir)

    for dir in dirs:
        bag_path = os.path.join(in_root, dir, "*.bag")
        new_bag_path = os.path.join(out_root, dir)

        if not os.path.exists(new_bag_path):
            os.makedirs(new_bag_path)

        for in_file in glob.glob(bag_path):
            file_name = in_file.split("/")[-1]
            out_file_path = os.path.join(new_bag_path, file_name)

            print(out_file_path)
            call(["rosbag", "fix", in_file, out_file_path, bmr_file])
