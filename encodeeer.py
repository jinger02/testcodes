

s = open('encoded.txt','w')


alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
key = 'xXzZnNlLwWeEbBgGjJhHqQdDyYvVtTkKfFuUoOmMpPcCiIaAsSrR'


secret_message = open('decoded.txt')

for item in secret_message:
    line = item
    
    for character in line:
        if character.isalpha():
            print(key[alphabet.index(character)],end='', file=s)
        else:
            print(character, end='', file=s)

    
s.close()

