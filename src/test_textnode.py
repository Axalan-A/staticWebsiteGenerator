import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_bad_url(self):
        node = TextNode("This is a test node", "link", "hello.com")
        node2 = TextNode("This is a test node", "link")
        self.assertNotEqual(node, node2)

    def test_bad_type(self):
        node = TextNode("testing node", "bold")
        node2 = TextNode("testing node", "italic")
        self.assertNotEqual(node, node2)

    def test_bad_text(self):
        node = TextNode("testing node", "bold")
        node2 = TextNode("testing bold", "bold")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
