from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f'LeafNode("{self.tag}", "{self.value}", {self.props})'
