from splitblocks import markdown_to_blocks, block_to_block_type
from textnode import text_node_to_html_node
from splitnodes import text_to_textnodes


def convert_heading(block):
    heading_level = block.count("#", 0, 6)
    heading_text = block[heading_level:].strip()
    heading_nodes = text_to_textnodes(heading_text)
    heading_html = "".join([text_node_to_html_node(node).to_html() for node in heading_nodes])
    return f'<h{heading_level}>{heading_html}</h{heading_level}>'

def convert_code(block):
    code_content = block[3:-3].strip()
    return f'<pre><code>{code_content}</code></pre>'

def convert_quote(block):
    quote_lines = block.split('\n')
    html_lines = []
    for line in quote_lines:
        line_content = line[1:].strip()
        line_nodes = text_to_textnodes(line_content)
        line_html = "".join([text_node_to_html_node(node).to_html() for node in line_nodes])
        html_lines.append(f'{line_html}')
    combined_quote = "\n".join(html_lines)
    return f'<blockquote>{combined_quote}</blockquote>'

def convert_unordered_list(block):
    list_items = block.split('\n')
    html_items = []
    for item in list_items:
        item_content = item[2:].strip()
        item_nodes = text_to_textnodes(item_content)
        item_html = "".join([text_node_to_html_node(node).to_html() for node in item_nodes])
        html_items.append(f'<li>{item_html}</li>')
    combined_list = "".join(html_items)
    return f'<ul>{combined_list}</ul>'

def convert_ordered_list(block):
    list_items = block.split('\n')
    html_items = []
    for item in list_items:
        item_content = item[3:].strip()
        item_nodes = text_to_textnodes(item_content)
        item_html = "".join([text_node_to_html_node(node).to_html() for node in item_nodes])
        html_items.append(f'<li>{item_html}</li>')
    combined_list = "".join(html_items)
    return f'<ol>{combined_list}</ol>'

def convert_paragraph(block):
    paragraph_nodes = text_to_textnodes(block)
    paragraph_html = "".join([text_node_to_html_node(node).to_html() for node in paragraph_nodes])
    return f'<p>{paragraph_html}</p>'

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    blocks_and_types = [(block, block_to_block_type(block)) for block in md_blocks]
    
    block_converters = {
        "text_type_Heading": convert_heading,
        "text_type_Code": convert_code,
        "text_type_Quote_Block": convert_quote,
        "text_type_Unordered_List": convert_unordered_list,
        "text_type_Ordered_List": convert_ordered_list,
    }
    
    html_blocks = []
    for block, block_type in blocks_and_types:
        converter = block_converters.get(block_type, convert_paragraph)
        html_blocks.append(converter(block))
    
    combined_html = "".join(html_blocks)
    return f'<div>{combined_html}</div>'
