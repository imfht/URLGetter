# encoding: utf-8
import sys
from urlparse import urldefrag
from urlparse import urljoin

import requests
from bs4 import BeautifulSoup
from gevent import monkey
from gevent.pool import Pool
from pybloom import BloomFilter

reload(sys)
sys.setdefaultencoding('utf-8')

monkey.patch_all()


class Worker():
    def __init__(self, urls):
        self.urls = urls
        self.new_urls = set()
        self.filter = BloomFilter(capacity=100000, error_rate=0.001)

    def get_urls(self, text):
        pass

    def fetch_url(self, url):
        try:
            req = requests.get(url, timeout=10)
        except:
            return
        soup = BeautifulSoup(req.text, 'html.parser')
        for tag in soup.find_all('a', {'href': True}):
            new_url = urldefrag(urljoin(url, tag.get('href')))[0]
            if not new_url.startswith('http'):
                continue
            if new_url not in self.filter:
                self.filter.add(new_url)
                print new_url

    def run(self):
        p = Pool(size=100)
        p.map(self.fetch_url, self.urls)


def test():
    urls = ['http://www.baidu.com', 'http://www.baidu.com', 'http://www.v2ex.com', 'http://www.sdu.edu.cn',
            'http://www.noexists.ccc']
    Worker(urls).run()


if __name__ == '__main__':
    Worker(urls=[i.strip() for i in open(sys.argv[1])]).run()
