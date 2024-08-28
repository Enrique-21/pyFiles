import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#enter the URL/position&reps that you want
url = input('Enter URL - ')
pos = int(input('Enter number of posistions: '))
reps = int(input('Enter number of repetitions: '))


#repeats 'reps' times
for x in range(reps):
    # opening url and let beautiful soup do its thing
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # gets all of the tags
    tags = soup('a')
    #adds one to count until it reaches 'reps' times
    count = 0
    for tag in tags:
        count = count + 1
        #once count is higher than pos it breaks
        if count > pos:
            break
        # pulls out the last name
        url = tag.get('href', None)
        name = tag.contents[0]
print(name)
        