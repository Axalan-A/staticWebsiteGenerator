from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("invalid format. delimitter not closed")
            # Oh wait. The delimited point will always be an even index
            for block in range(len(split_text)):
                if split_text[block].text == "":
                    continue
                if block % 2 == 1:
                    new_nodes.append(TextNode(split_text[block], text_type=text_type))
                else:
                    new_nodes.append(
                        TextNode(split_text[block], text_type=TextType.TEXT)
                    )
    return new_nodes
