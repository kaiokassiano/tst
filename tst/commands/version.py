import os
import sys
import requests
import pkg_resources
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache

from tst.utils import cprint
from tst.colors import *

def main():
    current = pkg_resources.get_distribution('tst').version
    if not sys.stdout.isatty():
        print(current)
        return

    cprint(WHITE, current, file=sys.stdout)
    try:
        s = requests.session()
        s = CacheControl(s, cache=FileCache(os.path.expanduser('~/.tst/cache')))
        response = s.get('https://pypi.org/pypi/tst/json')
        data = response.json()
    except requests.ConnectionError:
        pass

    latest_version = data['info']['version']
    if current != latest_version:
        cprint(YELLOW, 'Latest version available: %s' % latest_version, file=sys.stdout)
        cprint(RESET, '---\nUse `pip install --upgrade tst`')
        cprint(RESET, ' or `pip install --upgrade --user tst`')
