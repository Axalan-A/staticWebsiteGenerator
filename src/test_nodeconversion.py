import unittest
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node

class ConversionTests(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
