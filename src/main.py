from textnode import TextNode

def main():
    
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(textnode)


# Using the special variable 
# __name__
if __name__=="__main__":
    main()