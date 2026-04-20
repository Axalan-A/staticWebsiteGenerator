import os
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
    else:
        with open(dest_path, "x") as output_html:
            output_html.write(output_text)
