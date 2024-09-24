from splitblocks import markdown_to_blocks, block_to_block_type


def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    blocks_and_types = []
    html_blocks = []
    for block in md_blocks:
        blocks_and_types.append((block, block_to_block_type(block)))
    for block in blocks_and_types:
        if block[1] == "text_type_Heading":
            heading_level = 0
            for i in block[0][:6]:
                if i == "#":
                    heading_level += 1
            heading_text = block[0][heading_level:].strip()
            html_blocks.append(f'<h{heading_level}>{heading_text}</h{heading_level}>')
        elif block[1] == "text_type_Code":
            code_content = block[0][3:-3].strip()
            html_blocks.append(f'<pre><code>{code_content}</code></pre>')
        elif block[1] == "text_type_Quote_Block":
            quote_lines = block[0].split('\n')
            html_lines = []
            for line in quote_lines:
                line_content = line[1:].strip()
                html_lines.append(f'{line_content}')
            combined_quote = "\n".join(html_lines)
            html_blocks.append(f'<blockquote>{combined_quote}</blockquote>')
        elif block[1] == "text_type_Unordered_List":
            list_items = block[0].split('\n')
            html_items = []
            for item in list_items:
                item_content = item[2:].strip()
                html_items.append(f'<li>{item_content}</li>')
            combined_list = "".join(html_items)
            html_blocks.append(f'<ul>{combined_list}</ul>')
        elif block[1] == "text_type_Ordered_List":
            list_items = block[0].split('\n')
            html_items = []
            for item in list_items:
                item_content = item[3:].strip()
                html_items.append(f'<li>{item_content}</li>')
            combined_list = "".join(html_items)
            html_blocks.append(f'<ol>{combined_list}</ol>')
        else:
            html_blocks.append(f'<p>{block[0]}</p>')
    combined_html = "".join(html_blocks)
    div_node = f'<div>{combined_html}</div>'
    return div_node

            
  

