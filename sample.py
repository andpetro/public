# from lxml import etree as ET

# stream = open('sample.xml', 'r')

# xml = ET.parse(stream)

# root = xml.getroot()

# for e in root:
#     print(ET.tostring(e))
#     print("")
#     print(e.get("Id"))

import xmltodict

stream = open('sample.xml', 'r')

xml = xmltodict.parse(stream.read())

for e in xml["Person"]["telecom"]:
    print(e)



