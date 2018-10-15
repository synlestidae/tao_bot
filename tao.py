import requests
import re
from lxml.html import fromstring
from datetime import datetime

def section(text):
    re.compile("\d+\.\d+").match(text)         

def tao():
    tao_content = requests.get('http://www.mit.edu/~xela/tao.html').text
    children = fromstring(tao_content).find('body').iterchildren()
    body = []
    i = None
    for element in children:
        if not element.text: continue
        try:
            if i: 
                yield i, j, body
                body = []
            i, j = map(int, element.text.split('.'))
        except:
            if element.text: body.append(element.text) 

if __name__ == '__main__':
    for i, j, body in tao():
        print("%d.%d `%s`" % (i, j, '\n'.join(map(str.strip, body))))

