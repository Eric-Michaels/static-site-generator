import unittest
from markdowntohtml import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_heading(self):
        markdown = "# Heading 1"
        expected_html = "<div><h1>Heading 1</h1></div>"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result, expected_html)

    def test_code_block(self):
        markdown = "```code```"
        expected_html = "<div><pre><code>code</code></pre></div>"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result, expected_html)

    def test_multiline_code_block(self):
        markdown = "```\ncode line 1\ncode line 2\n```"
        expected_html = "<div><pre><code>code line 1\ncode line 2</code></pre></div>"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result, expected_html)

    def test_quote_block(self):
        markdown = "> This is a quote"
        expected_html = "<div><blockquote>This is a quote</blockquote></div>"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result, expected_html)

    def test_multiline_quote_block(self):
        markdown = "> This is a quote\n> This is another line of the quote"
        expected_html = "<div><blockquote>This is a quote\nThis is another line of the quote</blockquote></div>"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result, expected_html)

    def test_empty_input(self):
        markdown = ""
        expected_html = "<div></div>"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result, expected_html)

    def test_no_markdown_syntax(self):
        markdown = "This is a plain text"
        expected_html = "<div><p>This is a plain text</p></div>"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result, expected_html)

if __name__ == "__main__":
    unittest.main()