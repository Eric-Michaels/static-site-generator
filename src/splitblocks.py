import re
from enum import Enum

class BlockType(Enum):
    Heading = r'^#{1,6}'
    Code = r'^```[\s\S]*```$'
    Quote_Block = r'^(>.*\n?)*$'
    Unordered_List = r'^([*-] .*)$'
    Ordered_List = r'^(\d+)\.\s.'

def markdown_to_blocks(text):
    blocks = []
    normalized_text = text.replace('\r\n', '\n').replace('\r', '\n')
    blocks = re.split(r'\n\s*\n', normalized_text.strip())
    for block in blocks:
        if block == "":
            blocks.remove(block)

    return blocks

def block_to_block_type(block):
    for block_type in BlockType:
        pattern = block_type.value

        if block_type.name == "Ordered_List":
            result = check_ordered_list(block)
            if result:
                return result
        elif re.match(pattern, block, re.MULTILINE):
            return f"text_type_{block_type.name}"
    return "text_type_Paragraph"
        


def check_ordered_list(block):
    lines = block.split('\n')
    expected_number = 1
    pattern = r'^(\d+)\.\s.'

    for idx, line in enumerate(lines):
        match = re.match(pattern, line)
        if match:
            number = int(match.group(1))
            if number != expected_number:
                return False
            expected_number += 1
        else:
            return False
    return f"text_type_{BlockType.Ordered_List.name}"