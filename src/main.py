import os
import shutil

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
shutil.rmtree("public")
os.mkdir("public")

copy_site_files("static", "public")
# generate_page("content/index.md", "template.html", "public/index.html")
generate_page_recursive("content/", "template.html", "public/")
