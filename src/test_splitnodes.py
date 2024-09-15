import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.text)
        expected_nodes = [
            TextNode("This is text with a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is **bold** text", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.text)
        expected_nodes = [
            TextNode("This is ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" text", TextType.text),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is *italic* text", TextType.text)
        new_nodes = split_nodes_delimiter([node], "*", TextType.text)
        expected_nodes = [
            TextNode("This is ", TextType.text),
            TextNode("italic", TextType.italic),
            TextNode(" text", TextType.text),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_no_split(self):
        node = TextNode("This is plain text", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.text)
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_non_text_node(self):
        node = TextNode("This is plain text", TextType.bold)
        new_nodes = split_nodes_delimiter([node], "`", TextType.text)
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_unpaired_delimiter(self):
        node = TextNode("This is `unpaired code text", TextType.text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.text)

    def test_split_nodes_delimiter_multiple_delimiters(self):
        node = TextNode("This is `code` and **bold** text", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.text)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.text)
        expected_nodes = [
            TextNode("This is ", TextType.text),
            TextNode("code", TextType.code),
            TextNode(" and ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" text", TextType.text),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_empty_text_node(self):
        node = TextNode("", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.text)
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_mixed_content(self):
        nodes = [
            TextNode("This is ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" and `code` text", TextType.text)
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.text)
        expected_nodes = [
            TextNode("This is ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" and ", TextType.text),
            TextNode("code", TextType.code),
            TextNode(" text", TextType.text),
        ]
        self.assertEqual(new_nodes, expected_nodes)

if __name__ == '__main__':
    unittest.main()