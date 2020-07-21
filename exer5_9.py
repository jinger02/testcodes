#Exercise 1&2: Write a program which repeatedly reads numbers until the user enters "done".
#Once "done" is entered, print out the total, count, and average of the numbers.
#if the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

total = 0
count = 0
average = 0
largest = None
smallest = None
while True:
    line = input('Enter a number\n')
    if line == 'done':
        print('Total',total)
        print('Count',count)
        print ('average',average)
        print('smallest', smallest)
        print('largest', largest)
        break
    else:
        try:
            line = int(line)
            total = line + total
            count = count +1
            average = (total / count)
            for itervar in [line]:
                if smallest is None or itervar < smallest:
                    smallest = itervar
                if largest is None or itervar > largest:
                    largest = itervar
            continue
        except ValueError:
            print('Enter a number or done')
