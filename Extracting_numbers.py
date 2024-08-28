import re

#opens the file
fhand = open('regex_sum_1973580.txt')

sum = 0 
for line in fhand:
    #removes any white spaces from the sentences
    line = line.strip()
    #extracts the numbers
    x = re.findall('([0-9]+)', line)
    #adds the numbers together
    for number in x:
        x = int(number)
        sum = sum + x
    
print('The sum is:', sum)