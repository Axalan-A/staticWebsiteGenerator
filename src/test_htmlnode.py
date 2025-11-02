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
        pass
