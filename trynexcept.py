rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
    
if ival > 0 :
    print('Nice Job!')
else:
    print('You did not enter a digit number')