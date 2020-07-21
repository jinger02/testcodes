from string import punctuation

class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            s = s.replace(c, '')
        s = s.lower()
        self.words = s.split()

    def number_of_words(self):
        return len(self.words)

    def starts_with(self, s):
        count = 0
        for word in self.words:
            if word[0] == s:
                count = count + 1
        return(count)
    
    def repeat_words(self, t):
        value = 0
        for word in self.words: 
            if word == t:
                value = value + 1
        return value
            
    def number_with_length(self, n):
        number = 0
        for word in self.words:
            if len(word) == n:
                number = number + 1
        return (number)

    def most_words(self):
        d = dict()
        t = self.words
        l2 = list()
        for word in t:
            d[word] = d.get(word,0)+1
        l = list(d.items())
        for key, value in l:
            l2.append((value, key))
        l2.sort(reverse=True)
        
        return l2[:10]

s = open(input('Enter file name:\n'))
string = ''
for line in s:
    line = line.rstrip()
    string = string + ' ' + line

analyzer = Analyzer(string)
