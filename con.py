inp = input('Enter tempereature in farenheight\n')

try:
    far=float(inp)
    cel=(far-32.0)*5.0/9.0
    print(cel)

except:
    print('Please enter a number')
