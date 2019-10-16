# bag_migration
script to migrate ros bag

migrate.py is a really simple script

It can work only with this folder structure

-------------------------------------------
in_root
 - folder 1
    - bag1
    - bag2
    ....
 - folder 2
    - bag1
    - bag2
    ....
-------------------------------------------
out_root
 - folder 1
    - bag1
    - bag2
    ....
 - folder 2
    - bag1
    - bag2
    ....
-------------------------------------------

**Note: Please use folders inside the input root and output root as shown above
**Note: It is not necessary to create output folders.
**Note: This script doesn't work with multiple levels of sub-folders. (please implement graph search).

# How to run:

python migrate.py --in_root <in_root> --out_root <out_root> --bmr <bmr_filename>

# Fails

In case of failure, generate .bmr by yourself

Do this:

  rosbag check <rosbag_file> -g <rule_name.bmr>

  open the .bmr, replace valid = False with valid = True for all instances

  use this .bmr file with the migrate.py script
