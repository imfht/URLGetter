# URLGetter
dev ops engineer‘s url fetcher

## Getting Started
1. the main.py read urls from open(sys.argv[1])
2. then fetch the urls use gevent, BeautifulSoup will grep all links in source html(a tag only)
3. print each url

### Prerequisites

require python 2.7 && pip installed. For example

```
sudo apt install python-2.7 python-pip
```

### Installing
## clone the project

```
git clone https://github.com/fiht/URLGetter && cd URLGetter
```

## install requirement

```
sudo -H pip install requirements.txt
```

ps: vitrualenv maybe a better choice.

## run it

```
python main.py urls.txt
```

# Todo

- [x] print unique url (use [python-bloomfilter](https://github.com/jaybaird/python-bloomfilter))
- [ ] show process bar