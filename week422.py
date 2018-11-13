def rabbit(position,links):
    return (links[position-1])

def mahe(url):
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    ctx = ssl.create_default_context() #three lines to use HTTPS
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read() #context is also to use https

    soup = BeautifulSoup(html, 'html.parser')
    linklist = list()
    tags = soup('a')
    for tag in tags:
        url2 = tag.get('href', None)
        linklist.append(url2)
    return linklist

url = input('Enter:')
urls = list()
urls = mahe(url)
print(urls)
position = input('Enter positon:')
loop = input('Enter loop:')
loop = int(loop)
position = int(position)
while(loop != 0):
    link = rabbit(position,urls)
    print(link)
    urls = mahe(link)
    loop = loop - 1
