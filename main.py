# encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from urlparse import urldefrag
from urlparse import urljoin
import sys
import requests
from bs4 import BeautifulSoup
from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()


class Worker():
    def __init__(self, urls):
        self.urls = urls
        self.new_urls = set()

    def get_urls(self, text):
        pass

    def fetch_url(self, url):
        try:
            req = requests.get(url, timeout=10)
        except:
            return
        soup = BeautifulSoup(req.text, 'html.parser')
        for tag in soup.find_all('a', {'href': True}):
            url = urldefrag(urljoin(url, tag.get('href')))[0]
            if not url.startswith('http'):
                continue
            #self.new_urls.add(url)
            print url

    def run(self):
        p = Pool(size=100)
        p.map(self.fetch_url, self.urls)
        return filter(lambda x: x.startswith('http'), list(self.new_urls))


def test():
    urls = ['http://www.baidu.com', 'http://www.v2ex.com', 'http://www.sdu.edu.cn', 'http://www.noexists.ccc']
    new_urls = Worker(urls).run()
    for i in new_urls:
        print i


if __name__ == '__main__':
    Worker(urls=[i.strip() for i in open(sys.argv[1])]).run()
