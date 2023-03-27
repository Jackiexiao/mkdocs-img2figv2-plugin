# plugin.py

import re
from pathlib import Path

from mkdocs.plugins import BasePlugin


def modify_match(match, use_directory_urls):
    caption, image_link, attr_list = match.groups()
    if use_directory_urls:
        image_link = ('..' / Path(image_link)).as_posix()
    else:
        image_link = ('.' / Path(image_link)).as_posix()
    if attr_list:
        attr_list = attr_list.replace('{', '').replace('}', '')
    else:
        attr_list = ''

    return (
        r'<figure class="figure-image">'
        rf'  <img src="{image_link}" alt="{caption}" {attr_list}>'
        rf'  <figcaption>{caption}</figcaption>'
        r'</figure>'
    )


class Image2FigurePlugin(BasePlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_directory_urls = True

    def on_config(self, config):
        self.use_directory_urls = config['use_directory_urls']
        return config

    def on_page_markdown(self, markdown, **kwargs):
        pattern = re.compile(r'!\[(.*?)\]\((.*?)\)(\{[^\}]*\})?', flags=re.IGNORECASE)
        markdown = re.sub(pattern, lambda match: modify_match(match, self.use_directory_urls), markdown)
        return markdown
