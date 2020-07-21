x=float(input('Enter number of hours...\n'))

while True:

    try:
        type (x) != float
        print('Please enter a number')
     

    except:
        print ('Number of hours is', x)
        break
    
