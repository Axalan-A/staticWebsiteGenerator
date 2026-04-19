from block_to_blocktype import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node


def strip_text(text: str, type: BlockType) -> str:
    if type.name == "PARAGRAPH":
        return text
    elif type.name == "HEADER":
        split_text = text.split(" ")
        stripped_text = " ".join(split_text[1:])
        return stripped_text
    elif type.name == "CODE":
        return text[4:-3].strip()
    elif type.name == "QUOTE":
        return text[1:]
    elif type.name =="UNORDERED_LIST":
        split_text = text.split("\n")
        stripped_text = list(map(lambda text : text[2:], split_text)) # Remove the starting "- "
        return "\n".join(stripped_text)
    elif type.name =="ORDERED_LIST":
        split_text = text.split("\n")
        stripped_text = list(map(lambda text : text[3:], split_text)) # Remove the starting "x. "
        return "\n".join(stripped_text)
    else:
        split_lines = text.split("\n")
        split_lines = map(lambda text: text.strip(), split_lines)
        joined_string = " ".join(split_lines)
        return joined_string

def text_to_list_items(text:str) -> list[ParentNode]:
    split_list = text.strip("\n")
    list_items = []
    for item in list_items:
        text_nodes = text_to_textnodes(text)
        leaf_nodes = list(map(text_node_to_html_node, text_nodes))
        list_items.append(ParentNode(tag = "li", children = leaf_nodes))
    return list_items

def text_to_children(text: str, type: BlockType):
    if type.name == "HEADER":
        text_nodes = text_to_textnodes(strip_text(text, type))
        leaf_nodes = map(text_node_to_html_node, text_nodes)
        return list(leaf_nodes)
    elif type.name == "QUOTE":
        text_nodes = text_to_textnodes(strip_text(text, type))
        leaf_nodes = map(text_node_to_html_node, text_nodes)
        return list(leaf_nodes)
    elif type.name == "UNORDERED_LIST":
        return text_to_list_items(strip_text(text, type))
    elif type.name == "ORDERED_LIST":
        return text_to_list_items(strip_text(text, type))
    else:
        text_nodes = text_to_textnodes(strip_text(text, type))
        leaf_nodes = map(text_node_to_html_node, text_nodes)


def markdown_to_html_node(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == BlockType.HEADING:
            split_block = block.split(" ")
            header_level = split_block[0].count("#") # Get header level
            node = ParentNode(tag = f"h{header_level}", children = text_to_children(block, type))
        elif type == BlockType.CODE:
            code_node = text_node_to_html_node(TextNode(text_type = TextType.TEXT, text = strip_text(block, type)))
            node = ParentNode(tag = "pre", children = [ParentNode(tag = "code", children = code_node)])
        elif type == BlockType.QUOTE:
            node = ParentNode(tag = "blockquote", children = text_to_children(block, type))
        elif type == BlockType.UNORDERED_LIST:
            node = ParentNode(tag="ul", children = text_to_children(block, type))
        elif type == BlockType.ORDERED_LIST:
            node = ParentNode(tag="ol", children = text_to_children(block, type))
        else:
            node = ParentNode(tag = "p", children = text_to_children(block, type))

        children.append(node)
    parent_node = ParentNode(tag = "div", children = children)
    return parent_node.to_html()
