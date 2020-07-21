#while True:
#    fname = input('Enter the file name:')
#    try:
#        fhand = open(fname)
#        for line in fhand:
#            line = line.rstrip()
#            line = line.upper()
#            print(line)
#            if line.endswith('-0500'):
#                exit()
#    except:
#print('File cannot be opened:', fname)


fname = input('Enter the file name:')
count = 0
total = 0
try:
    fhand = open(fname)
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence'):
            values = float(line[20:])
            count = count + 1
            total = values + total
    print('Average:', total/count)
        
except:
    if fname == ('na na boo boo'):
        print('NA NA BOO BOO TO YOU - You have been punked!')
    else:
        print('File cannot be opened:', fname)
