import os
import shutil
from markdowntohtml import markdown_to_html_node

def main():
    dst = "./public"
    src = "./static"

    copy_files(src, dst)
    generate_page("./content/index.md", "./template.html", "./public/index.html")


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as file:
        src_content = file.read()
    with open(template_path, 'r') as file:
        template_content = file.read()
    html_content = markdown_to_html_node(src_content)
    title = extract_title(src_content)
    with open(dest_path, 'w') as file:
        file.write(template_content.replace("{{ Content }}", html_content).replace("{{ Title }}", title))
    


def copy_files(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst, copy_function=copy_and_print)

def copy_and_print(src, dst):
    print(f'Copying {src} to {dst}')
    return shutil.copy2(src, dst)
    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()