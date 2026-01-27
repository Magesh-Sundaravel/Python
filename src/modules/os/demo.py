import os
from datetime import datetime

# Get the current working directory
print(os.getcwd())

# List the files in the directory 
if os.path.exists("../os"):
    print(os.listdir("../os"))


# This will create a top level directory 
# Create a New directory 
if not os.path.exists("test"):
    os.mkdir("test")

# Delete the directory 
os.rmdir("test")

# If you want to create a directory from bottom level
# Then create a directory like this
if not os.path.exists("test_1/demo.py"):
    os.makedirs("test_1/demo.py")


# You can also delete the directory from bottom level as well.
if os.path.exists("test_1/demo.py"):
    os.removedirs("test_1/demo.py")


# # If you want to rename the file 
# if os.path.exists("demo_1.txt"):
#     os.rename("demo_1.txt","demo_2.txt")


# Stat of the file
print(f"Stat of the file : {os.stat("demo_1.txt")}")

# Size of the file
print(f"Size of the file : {os.stat("demo_1.txt").st_size}")

# Timestamp of the file
print(os.stat("demo_1.txt").st_mtime)


# Time stamp in human readable format
mod_time = os.stat("demo_1.txt").st_mtime
print(f"Datetime of the file : {datetime.fromtimestamp(mod_time)}")



# Walking in the directory 
for dir_path, dir_name, file_name in os.walk("../../../src"):
    print(f"Current Path : {dir_path}")
    print(f"Directory Name : {dir_name}")
    print(f"File Name : {file_name}")
    print("-" * 100)
        







