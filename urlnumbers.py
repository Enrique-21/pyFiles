from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#enter the URL that you want
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


sum = 0
#adds all contents that is received as numbers
tags = soup('span')

#counts all of the numbers in the html
for tag in tags:
    lines = ('Contents:', tag.contents[0])
    num = list(lines)
    y = int(num[1])
    #if the number is bigger than 0 it will add them together
    if y > 0:
        sum = sum + y
print(sum) 