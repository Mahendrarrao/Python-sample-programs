import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context() #three lines to use HTTPS
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter:')
html = urllib.request.urlopen(url, context=ctx).read() #context is also to use https
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('class', None))
