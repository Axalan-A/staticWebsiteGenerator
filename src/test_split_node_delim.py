import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class SplitDelimTests(unittest.TestCase):
        def test_text(self):
            node = TextNode("This is text with a `code block` word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
            self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ])

        def test_unclosed_delimiter(self):
            node = TextNode("Test without *delimiters uh oh!", TextType.TEXT)
            self.assertRaises(ValueError, lambda: split_nodes_delimiter([node], "*", TextType.BOLD))

        def test_two_italic(self):
            node = TextNode("This is text with _italicized words_ there might even be _two_", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
            self.assertEqual(new_nodes, [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("italicized words", TextType.ITALIC),
                TextNode(" there might even be ", TextType.TEXT),
                TextNode("two", TextType.ITALIC),
            ])

        def test_start_delim(self):
            node = TextNode("*This text* starts bold this time.", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
            self.assertEqual(new_nodes, [
                TextNode("This text", TextType.BOLD),
                TextNode(" starts bold this time.", TextType.TEXT)
            ]
)
