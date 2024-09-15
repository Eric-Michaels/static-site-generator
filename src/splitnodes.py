from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    split_type = ""
    if delimiter == "*":
        split_type = TextType.italic
    elif delimiter == "**":
        split_type = TextType.bold
    elif delimiter == "`":
        split_type = TextType.code   

    for node in old_nodes:
        if node.text_type != TextType.text:
            new_nodes.append(node)
            continue

        if delimiter in node.text:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Delimiter must be used in pairs")
                
            for i in range(len(split_text)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text[i], text_type))
                else:
                    new_nodes.append(TextNode(split_text[i], split_type))
        else:
            new_nodes.append(node)
    
    return new_nodes