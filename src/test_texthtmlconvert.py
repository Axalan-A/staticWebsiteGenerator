import unittest

from textnode import TextNode, TextType

class TextNodeConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This a bold node", TextType.BOLD_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This a bold node")

    def test_italic(self):
        node = TextNode("This a italic node", TextType.ITALIC_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This a italic node")

    def test_code(self):
        node = TextNode("This a code node", TextType.CODE_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This a code node")

    def test_link(self):
        node = TextNode("This a link node", TextType.LINK)
        html_node = node.text_node_to_html_node(props = {"href": "www.testlink.com"})
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This a link node")
        self.assertEqual(html_node.props, {"href":"www.testlink.com"})

    def test_linkerror(self):
        node = TextNode("This a link node", TextType.LINK)
        self.assertRaises(Exception, lambda: node.text_node_to_html_node())

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE)
        html_node = node.text_node_to_html_node(props = {"src": "img/folder", "alt": "test image"})
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "This is an image node")
        self.assertEqual(html_node.props, {"src":"img/folder", "alt":"test image"})





