import unittest

from src.extract_title import extract_title


class TestTitleExtraction(unittest.TestCase):
    def test_basic(self):
        title = "# Basic Title"
        extracted_title = extract_title(title)
        self.assertEqual("Basic Title", extracted_title)
