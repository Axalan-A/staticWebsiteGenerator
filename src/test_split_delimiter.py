import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestDelimiterSplit(unittest.TestCase):
    def test_codeblock(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(expected, new_nodes)
