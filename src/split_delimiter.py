from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        if text.count(delimiter) % 2 != 0:
            raise ValueError("Unclosed delimiter")
        splits = text.split(delimiter)
        for index in range(len(splits)):
            if splits[index] == "":
                continue
            if index % 2 == 1:
                new_node = TextNode(splits[index], text_type)

            else:
               new_node = TextNode(splits[index], TextType.TEXT)

            new_nodes.append(new_node)
    return new_nodes
