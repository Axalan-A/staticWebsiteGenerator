import unittest

from LeafNode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "Hello, world!")
        self.assertEqual(node.to_html(), "<code>Hello, world!</code>")

    def test_leaf_repr(self):
        node = LeafNode("link", "Hello, world!", {"link": "test.com"})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(\"link\", \"Hello, world!\", {'link': 'test.com'})",
        )
