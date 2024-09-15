import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_multi_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    

class TestLeafNode(unittest.TestCase):

    def test_leaf_node_value_none(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode(None, "a", {"href": "https://www.boot.dev"})
        self.assertEqual(str(context.exception), "LeafNode must have a value")

    def test_leaf_node_value_not_none(self):
        node = LeafNode("Link to boot.dev", "a", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Link to boot.dev</a>')

    def test_leaf_node_tag_none(self):
        node = LeafNode("Link to boot.dev", None, {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), 'Link to boot.dev')

class TestParentNode(unittest.TestCase):

    def test_parent_node_with_children(self):
        child1 = LeafNode("Child 1", "span")
        child2 = LeafNode("Child 2", "span")
        parent = ParentNode("div", [child1, child2])
        expected_html = '<div><span>Child 1</span><span>Child 2</span></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_node_with_props(self):
        child = LeafNode("Child", "span")
        parent = ParentNode("div", [child], {"class": "container"})
        expected_html = '<div class="container"><span>Child</span></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None)
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_parent_node_no_tag(self):
        child = LeafNode("Child", "span")
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [child])
        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_parent_node_empty_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [])
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_deeply_nested_structure(self):
        leaf1 = LeafNode("Leaf 1", "span")
        leaf2 = LeafNode("Leaf 2", "span")
        child = ParentNode("div", [leaf1, leaf2])
        parent = ParentNode("section", [child])
        expected_html = '<section><div><span>Leaf 1</span><span>Leaf 2</span></div></section>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_mixed_node_types(self):
        leaf = LeafNode("Leaf", "span")
        child = ParentNode("div", [leaf], {"class": "child-div"})
        parent = ParentNode("section", [leaf, child], {"class": "parent-section"})
        expected_html = '<section class="parent-section"><span>Leaf</span><div class="child-div"><span>Leaf</span></div></section>'
        self.assertEqual(parent.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()