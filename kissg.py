import os
import sys

import markdown

MARKDOWN_EXTENSION = '.md'
HTML_EXTENSION = '.html'
CWD = os.getcwd()
OUTPUT_FOLDER = 'out'

HEADER_PATH = os.path.join(CWD, 'templates', 'header.html')
FOOTER_PATH = os.path.join(CWD, 'templates', 'footer.html')

def get_all_filepaths_recursively(path):
    files = []
    for p in os.listdir(path):
        join_path = os.path.join(path, p)
        if os.path.isfile(join_path):
            files.append(join_path)
        elif os.path.isdir(join_path):
            files.extend(get_all_filepaths_recursively(join_path))
    return files

def filter_by_extension(files, extension):
    return [f for f in files if f.endswith(extension)]

def create_file_dict(files):
    res = {}
    for f in files:
        with open(f, 'r') as file:
            res[f] = file.read()
    return res

def get_slug(path):
    return path.split('/')[-1].split('.')[0]

def convert_markdown_to_html(markdown_string):
    return markdown.markdown(markdown_string)

if __name__ == '__main__':
    path = sys.argv[1]
    all_files = get_all_filepaths_recursively(path)
    markdown_files = filter_by_extension(all_files, MARKDOWN_EXTENSION)
    
    file_dict = create_file_dict(markdown_files)
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # load the header and footer
    with open(HEADER_PATH, 'r') as header_file:
        header = header_file.read()
    with open(FOOTER_PATH, 'r') as footer_file:
        footer = footer_file.read()
    
    # for each file in file_dict, create a new file in the output folder
    for f in file_dict:
        slug = get_slug(f)
        with open(os.path.join(OUTPUT_FOLDER, f"{slug}{HTML_EXTENSION}"), 'w') as file:
            html_body = convert_markdown_to_html(file_dict[f])
            html = header + html_body + footer
            file.write(html)