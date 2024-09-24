import unittest
from main import extract_title

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a title\nThis is a paragraph"
        result = extract_title(markdown)
        self.assertEqual(result, "This is a title")

    def test_extract_title_no_title(self):
        markdown = "This is a paragraph"
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()