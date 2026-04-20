import os
from pathlib import Path
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    # Read in the markdown file from "from_path"
    with open(from_path) as markdown_file:
        markdown_text = markdown_file.read()

    # Read template file from "template_path"
    with open(template_path) as template_file:
        template_text = template_file.read()

    markdown_as_html = markdown_to_html_node(markdown_text).to_html()
    webpage_title = extract_title(markdown_text)

    output_text = template_text.replace("{{ Title }}", webpage_title)
    output_text = output_text.replace("{{ Content }}", markdown_as_html)

    dest_folder = os.path.dirname(dest_path)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    print(f"Generating page: {from_path}\nTo: {dest_path}")
    with open(dest_path, "x") as output_html:
        output_html.write(output_text)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        target = os.path.join(dir_path_content, entry)
        if not os.path.isfile(target):
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_page_recursive(target, template_path, new_dest_dir)
    markdown_files = Path(dir_path_content).glob('*.md')
    for file in markdown_files:
        file_dest = os.path.join(dest_dir_path, "index.html")
        generate_page(file, template_path, file_dest)
