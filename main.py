import tinify
# from os import walk
import os
import imghdr
import shutil
from pathlib import Path

# TinyPNG apikey
tinify.key = "Z2t5P6cK9fV5HVVp2F1tQgqmxW5Z0Jgf"
# targetdir
root_dir = 'test_folder'
# the maximum size(in bytes) of the image the ones above are compressed
img_size_limit = 1000000  

# tynyfy by tinypng
def tinyfy_img(path):
    source = tinify.from_file(path)
    source.to_file("./tinyfied/" + path)
    print("tiny to " + "./tinyfied/" + path)

# print("======== WALK==========")
# root_dir = './test_folder'
# files = []
# for (dirpath, dirnames, filenames) in walk(root_dir):
#     files.extend(filenames)
#     print(dirpath)
#     print(dirnames)
#     print(filenames)
#     print("=========")
#     break


# print("======== SCANDIR ==========")
# directory = r'./test_folder'
# for entry in os.scandir(directory):
#     if entry.is_file():
#         print(entry.path)

# copy dir
def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
    print(f"dir {from_path} copied to {to_path}")

print("======== PATH RECOURSIVE ==========")

# copy root dir
copy_and_overwrite(root_dir, './tinyfied/' + root_dir)

paths = Path(root_dir).glob('**/*')
for path in paths:
    # because path is object not string
    path_in_str = str(path)
    if os.path.isfile(path):
        file_image_type = imghdr.what(path_in_str)
        if file_image_type != None:
            if (os.path.getsize(path_in_str) > img_size_limit ):
                print(path_in_str)
                tinyfy_img(path_in_str)
                print("============")

print("Tinyfied done 👍👍👍!")
