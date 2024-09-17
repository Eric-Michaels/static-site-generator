import unittest
from splitblocks import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def setUp(self):
        self.text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

    def test_empty_string(self):
        self.assertListEqual(markdown_to_blocks(""), [])

    def test_single_paragraph(self):
        single_paragraph_text = "# This is a heading"
        self.assertListEqual(markdown_to_blocks(single_paragraph_text), ["# This is a heading"])

    def test_multiple_paragraphs(self):
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertListEqual(markdown_to_blocks(self.text), expected)

    def test_mixed_line_endings(self):
        mixed_line_endings_text = self.text.replace('\n', '\r\n')
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertListEqual(markdown_to_blocks(mixed_line_endings_text), expected)

    def test_leading_trailing_whitespace(self):
        leading_trailing_whitespace_text = f"  \n\n  {self.text}  \n\n  "
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertListEqual(markdown_to_blocks(leading_trailing_whitespace_text), expected)

    def test_multiple_blank_lines(self):
        multiple_blank_lines_text = self.text.replace('\n\n', '\n\n\n\n')
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertListEqual(markdown_to_blocks(multiple_blank_lines_text), expected)

    def test_special_characters(self):
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertListEqual(markdown_to_blocks(self.text), expected)

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), "text_type_Heading")

    def test_code(self):
        block = "```\nThis is a code block\n```"
        self.assertEqual(block_to_block_type(block), "text_type_Code")

    def test_quote_block(self):
        block = "> This is a quote block\n> with multiple lines"
        self.assertEqual(block_to_block_type(block), "text_type_Quote_Block")

    def test_unordered_list(self):
        block = "* Item 1\n* Item 2\n* Item 3"
        self.assertEqual(block_to_block_type(block), "text_type_Unordered_List")

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), "text_type_Ordered_List")

    def test_paragraph(self):
        block = "This is a paragraph of text."
        self.assertEqual(block_to_block_type(block), "text_type_Paragraph")

    def test_incorrect_ordered_list(self):
        block = "1. First item\n3. Second item\n2. Third item"
        self.assertEqual(block_to_block_type(block), "text_type_Paragraph")

if __name__ == "__main__":
    unittest.main()