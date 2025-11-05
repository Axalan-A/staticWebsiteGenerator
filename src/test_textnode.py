import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This has a url", TextType.LINK, url="tester.com")
        node2 = TextNode(
            "This is a url too! But different text", TextType.LINK, url="tester.com"
        )
        self.assertNotEqual(node, node2)

    def test_blankURLeq(self):
        node = TextNode("This is the same url", TextType.LINK)
        node2 = TextNode("This is the same url", TextType.LINK)
        self.assertEqual(node, node2)

    def test_sameTextDiffLink(self):
        node = TextNode("This url goes here!", TextType.LINK, url="here.com")
        node2 = TextNode("This url goes here!", TextType.LINK, url="nothere.com")
        self.assertNotEqual(node, node2)

    def test_differentType(self):
        node = TextNode("Hello! I'm text!", TextType.BOLD)
        node2 = TextNode("Hello! I'm text!", TextType.ITALIC)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
