import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_no_children(self):
        parent_node = ParentNode("b", children=None)
        self.assertRaises(ValueError, lambda: parent_node.to_html())

    def test_multiple_children(self):
        child1 = LeafNode("p", "Hello! First paragraph")
        child2 = LeafNode("a", "This one's a link", {"href": "link.com"})
        child3 = LeafNode("p", "And then a closing paragraph")
        parent_node = ParentNode("div", children=[child1, child2, child3])
        expected = '<div><p>Hello! First paragraph</p><a href="link.com">This one\'s a link</a><p>And then a closing paragraph</p></div>'
        self.assertEqual(expected, parent_node.to_html())
