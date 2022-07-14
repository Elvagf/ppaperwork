import os
from fnmatch import fnmatch

###############################################################################

def hooks_before_user_overrides(worker):
    print("## Hooks before user overrides\n")
    append_dir_with_image_to_doxyfile(worker)
    print("\n")

###############################################################################

def append_dir_with_image_to_doxyfile(worker):
    print(" - Fill Doxygen IMAGE_PATH => needs to know where are the images to store them with html output")
    image_path=""
    for root, dirs, files in os.walk(worker.workDir):
        for dir in dirs:
            if dir == "img":
                dirpath = os.path.join(root, dir)
                dirpath = dirpath[len(worker.workDir)+1:]
                image_path += f" {dirpath}"
    worker.opts.doxyfile["IMAGE_PATH"] = image_path

###############################################################################

