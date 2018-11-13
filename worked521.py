import xml.etree.ElementTree as ET  #ET is something like a file handle for the tree

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>mehi</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>gloo</name>
        </user>
    </users>
</stuff>
'''     #''' is for multiline strings

data = ET.fromstring(input)
lst = data.findall('users/user')    #lst is a list of tags
for item in lst:
    name = item.find('name').text
    print(name)
