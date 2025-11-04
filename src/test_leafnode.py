import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        node = LeafNode("a","Click Me!", {"href": "https://www.google.com"})
        expected = "<a href=\"https://www.google.com\">Click Me!</a>"
        self.assertEqual(expected, node.to_html())
