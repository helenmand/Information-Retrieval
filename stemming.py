from csv import reader
import string
from greek_stemmer import stemmer

y = []

with open('test.txt','r', encoding='utf-8') as file:
    for line in file:   
        for word in line.split():         
            y.append(stemmer.stem_word(word.translate(str.maketrans('', '', string.punctuation)), 'VBG').lower())

print(len(y))
print(len(set(y)))