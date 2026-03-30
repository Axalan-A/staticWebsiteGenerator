import unittest
from extract_link import extract_markdown_images, extract_markdown_links

class ExtractionTests(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_wrong_func_link(self):
        matches = extract_markdown_images(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_wrong_func_image(self):
        matches = extract_markdown_links(
            "This is text with a ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)
    def test_brackets_in_link(self):
        matches = extract_markdown_links(
            "This is text with a [A link! with [these]](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("A link! with [these]", "https://i.imgur.com/zjjcJKZ.png")], matches)
