from split_delimiter import split_nodes_delimiter
from split_links import split_nodes_images, split_nodes_links
from textnode import TextNode, TextType


def text_to_textnodes(text: str):
    orig_node = TextNode(text=text, text_type=TextType.TEXT)
    nodes = split_nodes_delimiter([orig_node], text_type=TextType.BOLD, delimiter="**")
    nodes = split_nodes_delimiter(nodes, text_type=TextType.ITALIC, delimiter="_")
    nodes = split_nodes_delimiter(nodes, text_type=TextType.CODE, delimiter="`")
    nodes = split_nodes_links(old_nodes=nodes)
    nodes = split_nodes_images(old_nodes=nodes)
    return(nodes)
