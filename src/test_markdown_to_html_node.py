import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
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

    def test_quote(self):
        md = """
> This is a quote.
It should be properly quoted
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote. It should be properly quoted</blockquote></div>"
        )


    def test_list(self):
        md = """- List item.
- Next one.
- Then the last.

1. Now the first.
2. Then the second.
3. and the last third.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            first = html,
            second = """<div><ul><li>List item.</li><li>Next one.</li><li>Then the last.</li></ul><ol><li>Now the first.</li><li>Then the second.</li><li>and the last third.</li></ol></div>"""
        )

    def test_heading(self):
        md = """# This is h1

##### This is h5"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            first = html,
            second = "<div><h1>This is h1</h1><h5>This is h5</h5></div>"
        )
