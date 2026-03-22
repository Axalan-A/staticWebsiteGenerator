from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid Tag")
        if self.children == None:
            raise ValueError("Invalid Children")
        else:
            children_block = ""
            for child in self.children:
                children_block += child.to_html()
            return f"<{self.tag}>{children_block}</{self.tag}>"
