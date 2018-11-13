import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL:')
#url = urllib.parse.urlencode(url)
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
number = 0
count = 0
data =  data.decode()
tree = ET.fromstring(data)
results = tree.findall('./comments/comment') #Element.findall() finds only elements with a tag which are direct children of the current element
for item in results:
    #print(item.tag)
    number = item.find('count').text
    number = int(number)
    count = count + number
print('final:' ,count)
