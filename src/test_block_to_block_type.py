import unittest

from block_to_blocktype import BlockType, block_to_block_type


class TestBlockToBlocktype(unittest.TestCase):
    def test_heading(self):
        block = "#### This is a heading with 4 #s"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.HEADING)

    def test_not_heading(self):
        block = "####### This is paragraph starting with 7 #s"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_code(self):
        block = """```
        This is meant to be a code block
        ```"""
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.CODE)

    def test_not_code(self):
        block = """``` This shouldn't be a code block ```"""
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_quote(self):
        block = ">I am quoting something, this is a quote"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.QUOTE)

    def test_quote_with_space(self):
        block = "> I am quoting something, this is a quote but with a space"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.QUOTE)

    def test_unordered_list(self):
        block = """- List 1
- Then this
- Then that"""
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = """1. List 1
2. Then this
3. Then that"""
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.ORDERED_LIST)

    def test_not_ordered_list(self):
        block = """1. List 1
1. Then this
2. Then that"""
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.PARAGRAPH)
