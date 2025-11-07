import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_excessive_newlines(self):
        md = """
Hello! This one has so much lines!





I wonder
if it works?
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Hello! This one has so much lines!",
                "I wonder\nif it works?",
            ],
        )

    def test_markdown_excessive_spaces(self):
        md = """
This one has plenty of extra spaces          


        Any errors here?        
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This one has plenty of extra spaces",
                "Any errors here?",
            ],
        )
