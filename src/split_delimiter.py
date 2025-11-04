from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.value.split(delimiter)
            # Oh wait. The delimited point will always be an even index
            for block in range(0, len(split_text)):
                if block % 2 == 0:
                    new_nodes.append(TextNode(split_text[block], text_type=text_type))
                else:
                    new_nodes.append(
                        TextNode(split_text[block], text_type=TextType.TEXT)
                    )
