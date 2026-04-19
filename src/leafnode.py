from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag != None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return self.value

    def __repr__(self):
        return f'LeafNode("{self.tag}", "{self.value}", {self.props})'
