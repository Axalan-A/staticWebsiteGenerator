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
    # Split the block by space
    sections = block.split(" ")
    header_level = len(sections[0])
    return ParentNode(tag = f"h{header_level}", children = text_to_children(block[1:-1]))

# Every line of a quote block should begin with a >.
def quote_to_block(block):
    lines = block.split("\n")
    cleaned_text = ""
    for line in lines:
        cleaned_text += line.replace(">", "", 1)

    return ParentNode(tag = "quote", children = text_to_children(cleaned_text))

    # for line in lines:
    #     line = line[]
    # For each line, remove the > (should be the first character) then
    # rejoin the lines into a >-less string.

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
