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
    return ParentNode(tag = f"h{header_level}", children = text_to_children(block[header_level:]))

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
    # An unordered list will have the following characteristic:
    # All lines must begin with the character '-'
    #
    # So split the text by lines and remove the first character.
    # The children should all be tagged 'li'
    lines = block.split("\n")
    children = []
    for line in lines:
        cleaned_line = line.strip().replace("-", "", 1)
        children.append(ParentNode(tag = "li", children = text_to_children(cleaned_line)))
    return ParentNode(tag="ul", children = children)

def ordered_to_block(block):
    # An ordered list will have the following characteristic:
    # The first character of each line will consist of numbers counting up followed by a '.'
    # e.g. 1. followed by 2. then 3. then 4. and so on.
    #
    # We split the text into lines, remove the number and tag each line as 'li' as above.
    lines = block.split("\n")
    children = []
    for line in lines:
        num_end = line.find(".")
        children.append(ParentNode(tag = "li", children = text_to_children(text = line[num_end + 2:])))

    return ParentNode(tag="ol", children=children)

def code_to_block(block):
    text = block[3:-3].lstrip()
    return ParentNode(tag = "pre", children = [LeafNode(tag = "code", value =text)])

def paragraph_to_block(block):
    return ParentNode(tag ="p", children = text_to_children(block))


def block_to_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
       return heading_to_block(block)
    elif block_type == BlockType.QUOTE:
       return quote_to_block(block)
    elif block_type == BlockType.UNORDERED:
      return unordered_to_block(block)
    elif block_type == BlockType.ORDERED:
      return  ordered_to_block(block)
    elif block_type == BlockType.CODE:
      return  code_to_block(block)
    elif block_type == BlockType.PARAGRAPH:
      return paragraph_to_block(block)
    else:
        raise ValueError("Invalid Type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_node(block))
    return ParentNode(tag="div", children=html_nodes)
