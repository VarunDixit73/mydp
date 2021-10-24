'''
use the file for gutenberg to read and count the words and then store the answer in the new file like:
a=12
to=123
hi= 125

Make this a one or more function program
'''

def file_c(filename):
    file = open('filename')
    data = filename.read()
    words = data.split()
    print('Number of words in text file :', len(words))


file_c('frank.txt')
