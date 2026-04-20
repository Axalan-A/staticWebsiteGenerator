from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == "img" and self.props is not None:
            return f"<{self.tag} src={self.props["src"]} alt=\"{self.props["alt"]}\">"
        if self.tag == "a" and self.props is not None:
            return f"<{self.tag} href={self.props["href"]}>{self.value}</{self.tag}>"
        elif self.tag != None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return self.value

    def __repr__(self):
        return f'LeafNode("{self.tag}", "{self.value}", {self.props})'
