import urllib.request, urllib.parse, urllib.error

#opens the url
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#counts how many words are in the url
counts = dict()
for line in fhand:
    #must decode the url in order to change bytes-->UTF-8
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)