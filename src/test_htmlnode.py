import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_basic_case(self):
        node = HTMLNode("p", "Test paragraph", props = {"href": "test.com", "target": "blank"})
        result = node.props_to_html()
        expected = " href=\"test.com\" target=\"blank\""

        self.assertEqual(result, expected)

    def test_one_prop(self):
        node = HTMLNode(tag = "p", value = "Test", props = {"target": "none"})
        result = node.props_to_html()
        expected = " target=\"none\""

        self.assertEqual(result, expected)

    def test_repr(self):
        node = HTMLNode(tag = "p", value = "Test", props = {"target": "none"})
        result = node.__repr__()
        expected = "HTMLNode(\"p\", \"Test\", None, {\'target\': \'none\'})"

        self.assertEqual(result, expected)
