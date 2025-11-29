from htmlnode import ParentNode, LeafNode
from markdown_to_blocks import markdown_to_blocks
from blockType import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

def text_to_children(text, list=False):
    text_nodes = text_to_textnodes(text.replace("\n", " ").strip())
    leaves = []
    for node in text_nodes:
        if list:
            node.tag = "li"
        leaves.append(node.text_node_to_html_node())
    return leaves


def block_to_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        sections = block.split(" ")
        tag = f"h{len(sections[0])}"
    elif block_type == BlockType.QUOTE:
        tag = "blockquote"
    elif block_type == BlockType.UNORDERED:
        tag = "ul"
        return ParentNode(tag=tag, children=text_to_children(block, list=True))
    elif block_type == BlockType.ORDERED:
        tag = "ol"
        return ParentNode(tag=tag, children=text_to_children(block, list=True))
    elif block_type == BlockType.CODE:
        tag = "code"
        return ParentNode(
            tag="pre",
            children=ParentNode(
                tag=tag, children=TextNode(text=block, text_type=TextType.TEXT)
            ),
        )
    elif block_type == BlockType.PARAGRAPH:
        tag = "p"
    else:
        raise ValueError("Invalid Type")

    return ParentNode(tag=tag, children=text_to_children(block))


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_node(block))
    return ParentNode(tag="div", children=html_nodes)
