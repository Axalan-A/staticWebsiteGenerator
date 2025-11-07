def markdown_to_blocks(markdown):
    blocks_to_process = markdown.split("\n\n")
    final_blocks = []
    for block in blocks_to_process:
        if block == "":
            continue
        block = block.strip()
        final_blocks.append(block)
    return final_blocks
