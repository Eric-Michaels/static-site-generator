import unittest
from textnode import TextNode, text_node_to_html_node, TextType
from htmlnode import LeafNode, ParentNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_default_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)
    
    def test_neq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_neq_different_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")


class TestTextToHTML(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        node = TextNode("Hello", TextType.text)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.to_html(), "Hello")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("Hello", TextType.bold)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, ParentNode)
        self.assertEqual(html_node.to_html(), "<b>Hello</b>")

    def test_text_node_to_html_node_italic(self):
        node = TextNode("Hello", TextType.italic)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, ParentNode)
        self.assertEqual(html_node.to_html(), "<i>Hello</i>")

    def test_text_node_to_html_node_code(self):
        node = TextNode("Hello", TextType.code)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, ParentNode)
        self.assertEqual(html_node.to_html(), "<code>Hello</code>")

    def test_text_node_to_html_node_link(self):
        node = TextNode("Hello", TextType.link, url="http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, ParentNode)
        self.assertEqual(html_node.to_html(), '<a href="http://example.com">Hello</a>')

    def test_text_node_to_html_node_image(self):
        node = TextNode("Image", TextType.image, url="http://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.to_html(), '<img src="http://example.com/image.png" alt="Image"></img>')

if __name__ == "__main__":
    unittest.main()