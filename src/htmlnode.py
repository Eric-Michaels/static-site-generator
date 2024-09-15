
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if isinstance(self.props, dict):
            prop_list = []
            for k, v in self.props.items():
                prop_list.append( f'{k}="{v}"')
            return ' ' + ' '.join(prop_list)
        else:
            return ''
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)
        if value is None:
            raise ValueError("LeafNode must have a value")
    def to_html(self):
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag")
        if not children:
            raise ValueError("ParentNode must have children")
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        children_html_list = []
        for child in self.children:
            children_html_list.append(child.to_html())
        return f"<{self.tag}{self.props_to_html()}>{''.join(children_html_list)}</{self.tag}>"