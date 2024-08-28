import json, urllib.request

address = input('Enter location: ') 
print('Retrieving', address)

#opens the location and turns the data found form UTF-8 into unicode
url = urllib.request.urlopen(address)
data = json.loads(url.read().decode())


#prints characters found in "comments" section
print('Retrieved', len(str(data)), 'characters')
x = data.get("comments")

count = 0
total = 0

for items in range(len(x)):
    y = x[items]
    #extracts the number in "count"
    num = y.get("count")
    count = count + 1
    total = total + int(num)
    
print('Count: ', count)
print('Sum: ', total)
    