import unittest
from markdown_to_htmlnode import markdown_to_html_node


class TestMarkdownToHTMLNodes(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headers(self):
        md = """
### This should be in a h3 tag.

# This should be another in an h1 tag.


###### This should be an h6
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This should be in a h3 tag.</h3><h1>This should be another in an h1 tag.</h1><h6>This should be an h6</h6></div>",
        )

    def test_lists(self):
        md = """
- Apple
- Cabbage
- Grocery list
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Apple</li><li>Cabbage</li><li>Grocery list</li></ul></div>",
        )

    def test_orderedlists(self):
        print("Running!")
        md = """
1. Apple
2. Cabbage
3. Grocery list
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Apple</li><li>Cabbage</li><li>Grocery list</li></ol></div>",
        )

    def test_orderedlists(self):
        print("Running!")
        md = """Hello! Just a regular old paragraph here"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<p>Hello! Just a regular old paragraph here</p>",
        )
