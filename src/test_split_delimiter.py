from typing import Text
import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestDelimiterSplit(unittest.TestCase):
    def test_codeblock(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(expected, new_nodes)

    def test_closure(self):
        node = TextNode(
            text="This is text with an *unclosed bold", text_type=TextType.TEXT
        )
        self.assertRaises(
            ValueError, lambda: split_nodes_delimiter([node], "*", TextType.BOLD)
        )

    def test_multipleNodes(self):
        node1 = TextNode("*Bold!* Hello!", TextType.TEXT)
        node2 = TextNode("Also *bold!*", TextType.TEXT)
        node3 = TextNode("This is *the last* bold", TextType.TEXT)
        nodes = [node1, node2, node3]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        expected = [
            TextNode("Bold!", TextType.BOLD),
            TextNode(" Hello!", TextType.TEXT),
            TextNode("Also ", TextType.TEXT),
            TextNode("bold!", TextType.BOLD),
            TextNode("This is ", TextType.TEXT),
            TextNode("the last", TextType.BOLD),
            TextNode(" bold", TextType.TEXT),
        ]
        self.assertEqual(expected, new_nodes)
