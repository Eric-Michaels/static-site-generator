from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, extract_markdown_links, extract_markdown_images, text_to_textnodes

def main():
    
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(textnode)

    htmlnode = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
    print(htmlnode.props_to_html())

    leafnode = LeafNode("Link to boot.dev", "a", {"href": "https://www.boot.dev"})
    print(leafnode.to_html())

    parentnode = ParentNode("div", [leafnode], {"class": "container"})
    print(parentnode.to_html())

    split_nodes_delimiter([TextNode("Hello", "text"), TextNode("world", "bold")], "*", "italic")
    print(split_nodes_delimiter([TextNode("Hello", "text"), TextNode("world", "bold")], "*", "italic"))

    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(":::::::::::::::::::::::::::::::::::")
    print(text_to_textnodes(text))

# Using the special variable 
# __name__
if __name__=="__main__":
    main()