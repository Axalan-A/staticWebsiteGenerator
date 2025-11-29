from htmlnode import ParentNode, LeafNode
from markdown_to_blocks import markdown_to_blocks
from blockType import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

def text_to_children(text):
    text_nodes = text_to_textnodes(text.replace("\n", " ").strip())
    leaves = []
    for node in text_nodes:
        leaves.append(node.text_node_to_html_node())
    return leaves

def heading_to_block(block):
    pass

def quote_to_block(block):
    pass

def unordered_to_block(block):
    pass

def ordered_to_block(block):
    pass

def code_to_block(block):
    pass

def paragraph_to_block(block):
    pass


def block_to_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        heading_to_block(block)
    elif block_type == BlockType.QUOTE:
        quote_to_block(block)
    elif block_type == BlockType.UNORDERED:
        unordered_to_block(block)
    elif block_type == BlockType.ORDERED:
        ordered_to_block(block)
    elif block_type == BlockType.CODE:
        code_to_block(block)
    elif block_type == BlockType.PARAGRAPH:
        paragraph_to_block(block)
    else:
        raise ValueError("Invalid Type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_node(block))
    return ParentNode(tag="div", children=html_nodes)
