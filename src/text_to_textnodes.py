from split_delimiter import split_nodes_delimiter
from split_nodeLinks import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType


def text_to_textnodes(text):
    original_node = TextNode(text, text_type=TextType.TEXT)
    temp = split_nodes_delimiter(
        [original_node], delimiter="**", text_type=TextType.BOLD
    )
    temp = split_nodes_delimiter(temp, delimiter="_", text_type=TextType.ITALIC)
    temp = split_nodes_delimiter(temp, delimiter="`", text_type=TextType.CODE)
    temp = split_nodes_image(temp)
    temp = split_nodes_link(temp)
    return temp
