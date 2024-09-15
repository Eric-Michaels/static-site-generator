from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(textnode)

    htmlnode = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
    print(htmlnode.props_to_html())

    leafnode = LeafNode("Link to boot.dev", "a", {"href": "https://www.boot.dev"})
    print(leafnode.to_html())

    parentnode = ParentNode("div", [leafnode], {"class": "container"})
    print(parentnode.to_html())

# Using the special variable 
# __name__
if __name__=="__main__":
    main()