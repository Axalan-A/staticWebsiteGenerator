import unittest

from htmlnode import HTMLNode

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
