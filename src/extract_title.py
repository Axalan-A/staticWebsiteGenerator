from block_to_blocktype import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from markdown_to_html_node import strip_text


def extract_title(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            words = block.split(" ")
            if words[0].count("#") == 1:
                return strip_text(block, type = BlockType.HEADING)
    raise Exception("No h1 title found.")
