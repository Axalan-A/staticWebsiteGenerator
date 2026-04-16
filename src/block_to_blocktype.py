from enum import Enum


class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6


def check_unordered_list(block:str) -> bool:
    lines = block.split("\n")
    for line in lines:
        if line[0:2] != "- ":
            return False
    return True

def check_ordered_list(block:str) -> bool:
    counter = 1
    lines = block.split("\n")
    for line in lines:
        if line[0:3] != f"{counter}. ":
            return False
        counter += 1
    return True


def block_to_block_type(block: str):
    # Header testing
    words = block.split(" ")
    if 1 <= words[0].count("#") <= 6:
        return BlockType.HEADING
    elif block[0:4] == "```\n" and block[-3:] == "```":
        return BlockType.CODE
    elif block[0] == ">":
        return BlockType.QUOTE
    elif check_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif check_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
