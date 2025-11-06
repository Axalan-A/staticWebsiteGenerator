from textnode import TextNode, TextType
from extract_links import extract_markdown_links, extract_markdown_images


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        properties = extract_markdown_images(node.text)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(properties) == 0:
            new_nodes.append(node)
            continue
        sections = original_text.split(f"![{properties[0][0]}]({properties[0][1]})", 1)

        if len(properties) > 1:
            for property_index in range(1, len(properties)):
                alt_text = properties[property_index][0]
                image_link = properties[property_index][1]
                sections.extend(sections.pop().split(f"![{alt_text}]({image_link})", 1))

        current_image = 0
        for section_index in range(len(sections)):
            section = sections[section_index]
            if section_index != len(sections) - 1:
                if section != "":
                    new_nodes.append(TextNode(text=section, text_type=TextType.TEXT))
                alt_text = properties[current_image][0]
                image_link = properties[current_image][1]
                new_nodes.append(
                    TextNode(text=alt_text, url=image_link, text_type=TextType.IMAGE)
                )
                current_image += 1
            else:
                if section != "":
                    new_nodes.append(TextNode(text=section, text_type=TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        properties = extract_markdown_links(node.text)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(properties) == 0:
            new_nodes.append(node)
            continue
        sections = original_text.split(f"[{properties[0][0]}]({properties[0][1]})", 1)

        if len(properties) > 1:
            for property_index in range(1, len(properties)):
                anchor = properties[property_index][0]
                url = properties[property_index][1]
                sections.extend(sections.pop().split(f"[{anchor}]({url})", 1))

        current_image = 0
        for section_index in range(len(sections)):
            section = sections[section_index]
            if section_index != len(sections) - 1:
                if section != "":
                    new_nodes.append(TextNode(text=section, text_type=TextType.TEXT))
                anchor = properties[current_image][0]
                url = properties[current_image][1]
                new_nodes.append(
                    TextNode(text=anchor, url=url, text_type=TextType.LINK)
                )
                current_image += 1
            else:
                if section != "":
                    new_nodes.append(TextNode(text=section, text_type=TextType.TEXT))
    return new_nodes
