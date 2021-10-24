'''
use the file for gutenberg to read and count the words and then store the answer in the new file like:
a=12
to=123
hi= 125

Make this a one or more function program
'''

from string import punctuation

def question1_solver(read_file_path,save_file_path='result.txt'):
    # read the file and store in a variable
    file = open(read_file_path, encoding='utf-8')
    content = file.read()
    file.close()

    # remove every punctuations
    for punc in punctuation:
        content= content.replace(punc,'')

    # make every thing lowercase and split file in words
    words = content.casefold().split()
    print(f'total words => {len(words)}')

    # create a empty file
    with open(save_file_path,'w') as file2: # create
        # counting the words
        for word in set(words):
            count = words.count(word)           # creating words
            file2.write(f'{word}\t{count}\n')   # storing in file

# the end

question1_solver('frank.txt')
