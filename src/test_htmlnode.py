import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag = "p", value = "Hello, I am text")
        expected = """
        Type: p
        Value: Hello, I am text
        Children: None
        Props: None
        """
        actual = repr(node)
        self.assertEqual(actual, expected)

    def test_props(self):
        node = HTMLNode(props = {"href": "https://www.google.com", 
                                 "target": "_blank"})
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_noprops(self):
        node = HTMLNode()
        expected = ""
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        node = LeafNode("a","Click Me!", {"href": "https://www.google.com"})
        expected = "<a href=\"https://www.google.com\">Click Me!</a>"
        self.assertEqual(expected, node.to_html())
