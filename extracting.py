import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')

#Just shows "Retrieving..." and inserts the url you put in
print('Retrieving', url)

#reads all the data that is in the url you just entered
uh = urllib.request.urlopen(url)
data = uh.read()

#shows the amount of characters that it received
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)


sums = 0
count = 0
# counts all the data and gets the sum of the data
lst = tree.findall('comments/comment')
for itm in lst:
    count = count + 1
    x = itm.find('count').text
    sums = sums + int(x)

#prints the output
print('Count:', count)
print('Sum:', sums)
