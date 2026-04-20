import os
import shutil
import sys

from generate_page import generate_page, generate_page_recursive

def copy_site_files(path, target):
    # Now, look through static and begin copying
    static_files = os.listdir(path)
    for file in static_files:
        current_path = os.path.join(path, file)
        destination_path = os.path.join(target, file)
        if not os.path.isfile(current_path):
            print(f"Creating directory {destination_path}")
            new_target = os.path.join(target, file)
            os.mkdir(destination_path)
            copy_site_files(current_path, new_target)
        else:
            print(f"Copying file {current_path} to {destination_path}")
            shutil.copy(current_path, destination_path)

# Loop through all files/folders in public:
shutil.rmtree("docs")
os.mkdir("docs")

if len(sys.argv) == 1:
    basepath = "/"
else:
    basepath = sys.argv[1]

copy_site_files("static", "docs")
generate_page_recursive("content/", "template.html", "docs/", basepath)
