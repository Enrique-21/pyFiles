import xml.etree.ElementTree as ET
data = '''<person>
  <name>Enrique</name>
  <phone type="intl">
     +1 219 718 2701
  </phone>
  <email hide = "yes"/>
</person>'''

tree = ET.fromstring(data)
print ('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))