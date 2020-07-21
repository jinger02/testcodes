#Exercise 35:Dog Years


print('Dog years')
print('This converts human years in dog years')

old = input('Input age of dog in human years\n')

try:
    dogyrs = int(old)
    if dogyrs ==1:
        print('Age in Dog years is 7.')
    if dogyrs >=2:
        print('Age in dog years is',10.5 +((dogyrs-2)*4))
    elif dogyrs< 0:
        print('Please enter a positive number\n')
except:
    print('Please input a number')
