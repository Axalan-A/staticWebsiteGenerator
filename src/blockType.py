from enum import Enum


class BlockType(Enum):
    PARAGRAPH = ("paragraph",)
    HEADING = ("heading",)
    CODE = ("code",)
    QUOTE = ("quote",)
    UNORDERED = ("unordered",)
    ORDERED = "ordered"


def block_to_block_type(block):
    quote = True
    unordered = True
    ordered = True
    sections = block.split(" ")
    lines = block.split("\n")
    num = 1
    for line in lines:
        if line == "":
            continue
        if line[0] != ">" and quote:
            quote = False
        if line[0] != "-" and unordered:
            unordered = False
        if line[0:2] == f"{num}." and ordered:
            num += 1
        else:
            ordered = False

    if "#" in set(sections[0]) and len(set(sections[0])) == 1 and len(sections[0]) <= 6:
        return BlockType.HEADING
    elif block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    elif quote:
        return BlockType.QUOTE
    elif unordered:
        return BlockType.UNORDERED
    elif ordered:
        return BlockType.ORDERED
    else:
        return BlockType.PARAGRAPH
