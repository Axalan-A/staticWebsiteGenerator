def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n") # Split on double newlines
    output_blocks: list[str] = []
    for block in blocks:
        if block.strip() != "":
            output_blocks.append(block.strip())
    return output_blocks
