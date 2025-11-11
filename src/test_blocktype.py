import unittest

from blockType import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_header(self):
        md = "### Test hello"
        actual = block_to_block_type(md)
        self.assertEqual(actual, BlockType.HEADING)

    def test_heading_extraSpace(self):
        md = "###          Test hello"
        actual = block_to_block_type(md)
        self.assertEqual(actual, BlockType.HEADING)

    def test_heading_extrahash(self):
        md = "######## Test hello"
        actual = block_to_block_type(md)
        self.assertEqual(actual, BlockType.PARAGRAPH)

    def test_code(self):
        md = """```Test code block maybe with
line or two```"""
        actual = block_to_block_type(md)
        self.assertEqual(actual, BlockType.CODE)

    def test_quote(self):
        md = """>I'm quoting you now I guess
> Quote and quote
> End of quote."""
        actual = block_to_block_type(md)
        self.assertEqual(actual, BlockType.QUOTE)

    def test_unordered(self):
        md = """- Hello
- this
- is
- a
- test"""
        actual = block_to_block_type(md)
        self.assertEqual(actual, BlockType.UNORDERED)

    def test_ordered(self):
        md = """1. Hello!
2. I hope this works
3. Would be a shame if it didn't"""
        actual = block_to_block_type(md)
        self.assertEqual(actual, BlockType.ORDERED)

    def test_paragraph(self):
        md = """``` Hopefully this matches nothing of the patterns
- that I had added
1. To the finder.
### Surely though it should work out. `"""
        actual = block_to_block_type(md)
        self.assertEqual(actual, BlockType.PARAGRAPH)
