from extract_link import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(node.text)
        if images == []:
            continue
        for image in images:
            alt_text = image[0]
            image_url = image[1]
            splits = text.split(f"![{alt_text}]({image_url})", 1)
            if splits[0] != "":
                new_nodes.append(TextNode(text= splits[0],text_type = TextType.TEXT))
            new_nodes.append(TextNode(text=alt_text,text_type = TextType.IMAGE,url = image_url))
            text = splits[-1]
        if text != "":
            new_nodes.append(TextNode(text= text[0],text_type = TextType.TEXT))
    if new_nodes != []:
        return new_nodes
    else:
        return old_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(node.text)
        if links == []:
            continue
        for link in links:
            alt_text = link[0]
            link_url = link[1]
            splits = text.split(f"[{alt_text}]({link_url})", 1)
            if splits[0] != "":
                new_nodes.append(TextNode(text= splits[0],text_type = TextType.TEXT))
            new_nodes.append(TextNode(text=alt_text,text_type = TextType.LINK,url = link_url))
            text = splits[-1]
        if text != "":
            new_nodes.append(TextNode(text= text[0],text_type = TextType.TEXT))
    if new_nodes != []:
        return new_nodes
    else:
        return old_nodes
