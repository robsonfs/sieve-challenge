import re

def is_valid_url(url):
    regex = re.compile(r'^(http|https)://(\w+)\.(\w+)')
    return bool(re.search(regex, url))
