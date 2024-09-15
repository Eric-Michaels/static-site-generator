from enum import Enum
from htmlnode import LeafNode, ParentNode

TextType = Enum("TextType", ["text", "bold", "italic", "code", "link", "image"])

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.text:
            return LeafNode(text_node.text)
        case TextType.bold:
            return ParentNode("b", [LeafNode(text_node.text)])
        case TextType.italic:
            return ParentNode("i", [LeafNode(text_node.text)])
        case TextType.code:
            return ParentNode("code", [LeafNode(text_node.text)])
        case TextType.link:
            return ParentNode("a", [LeafNode(text_node.text)], {"href": text_node.url})
        case TextType.image:
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})

