#!/usr/bin/env python3
import kissg
import markdown as _markdown

from enum import Enum
# TODO add types everywhere

class DocumentType(Enum):
    HTML,
    CSS,
    JS

class Document:
    # has the attribute self.type: DocumentType
    def load(path): ...
    def dump(path): ...

    # only possible if loaded
    def absolute_path(): ...
    def slug(): ...

    def uglify(): ...
    def beautify(): ...

class HTMLDocument(Document):
    def set_title(new_title): ...
    def set_head_attribute(attr): ...

    def fill(key, value, escape_html = False): ...

    def beautify(): ...
    def uglify(): ...

    def to_markdown(): ...

class MarkdownDocument(Document):
    def get_metadata_all(): ... # front matter
    def get_metadata(key): ... # None if not existing

    def to_html(): ...

def get_markdown_files(path, recursive = True): ...
def mass_convert_markdown(path): ...

"""
Ideas/Open Problems:
    - Some dict mapping? Seems to restrictive
    - add a recipe part of the documentation with stuff like @tailwindcss/typography
    - make it all copy-pastable in a big readme to make sure that noone actually has to read the docs
    - if we want to do sane `markdown_path->html_path` mapping we need to save where the recursive
      translation began, since we cant just use the full absolute path :D
    - Check what jinja2 can actually do; check how you would map it to this workflow
        - Loops? Conditionals?
        - reremember how flask did it
"""

"""
The actual use case:

- First, a custom index.html with customly styled text
    - this styling should be possible using jinja2
    - This one has a few links, a few socials and a navbar
- Navbar:
    - About me:
        - The "index.html", about him
        - Previous Work
        - Impossible List
        - Now-Page
    - blog
        - The "index.html", creating a 2x2 grid of all his posts with a short header
            - Those should have metadata exposed from the front-matter
            - the front matter should allow any kind of metadata that then can be set via key-value
            - those should be only mapped to a markdown file. The front-matter should not be connected to the template
    - diary
        - Like blog, but different folder and also different base
        - since this is artsy, it also doesnt share any js or css with the more serious blog
    - cv
        - a manually crafted file that was written self-contained, nothing to do with jinja2
            - unsure whether this needs an exception or this should just be a template without variables
"""
