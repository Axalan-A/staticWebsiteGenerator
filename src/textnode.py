from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(self, props=None):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD_TEXT:
                return LeafNode("b", self.text)
            case TextType.ITALIC_TEXT:
                return LeafNode("i", self.text)
            case TextType.CODE_TEXT:
                return LeafNode("code", self.text)
            case TextType.LINK:
                if props is not None:
                    return LeafNode("a", self.text, props={"href": props["href"]})
            case TextType.IMAGE:
                if props is not None:
                    return LeafNode("img", value=None, props={"src": props["src"], "alt":props["alt"]})
