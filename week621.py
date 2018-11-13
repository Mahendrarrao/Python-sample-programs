import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL:')
#url = urllib.parse.urlencode(url)
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
number = 0
count = 0
data =  data.decode()

info = json.loads(data)
print(json.dumps(info, indent = 2))

for item in info["comments"]:
    number = int(item["count"])
    count =  count + number

print(count)
