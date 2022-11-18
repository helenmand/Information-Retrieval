from greek_stemmer import stemmer
from collections import Counter
import sys

def punctuation_removal(Data):
    preprocessed_data = []
    preprocessed_data = Data.replace(',', ' ').replace('.', ' ').replace('-', ' ').replace('–', ' ').\
    replace(':', ' ').replace('«', ' ').replace('»', ' ').replace(';', ' ').replace('!', ' ').replace('…',' ').\
    replace('\t', ' ').replace('\b', ' ').replace('\xa0', ' ').replace('έ','ε').replace('ά','α').replace('ή','η').replace('ό','ο').\
    replace('ύ','υ').replace('ί','ι').replace('ώ','ω').replace('Ό','ο').replace('Έ','ε').replace('Ά','α').replace('Ή','η').\
    replace('Ύ','υ').replace('Ί','ι').replace('Ώ','ω').lower()
    preprocessed_data = preprocessed_data.split(' ')
    preprocessed_data = [word for word in preprocessed_data if word != '' and word != ' ' and word.isalpha()]
    return preprocessed_data

def stop_word_removal(preprocessed_data, stop_words_array):
    preprocessed_data1 = []
    stop_words_array = []
    preprocessed_data1 = preprocessed_data
    for stopword in stop_words_array:
        preprocessed_data1 = [word for word in preprocessed_data1 if word != stopword]
    preprocessed_data1 = ' '.join(preprocessed_data1)                          
    return preprocessed_data1

def stemming(preprocessed_data):
    preprocessed_data1 = []
    index = 0
    preprocessed_data = preprocessed_data.split(' ')
    for word in preprocessed_data:
        stemmed_word = stemmer.stem_word(word, 'VBG')
        if stemmed_word.islower():
            del preprocessed_data[index]
        else:
            preprocessed_data[index] = stemmed_word
        index += 1
    preprocessed_data1 = preprocessed_data      
    return preprocessed_data1            

def process(Data, stop_words_array):

    preprocessed_data = stop_word_removal(punctuation_removal(Data), stop_words_array)
    processed_data = stemming(preprocessed_data)

    data_list = preprocessed_data.split(' ')
    word_frequency = Counter(data_list)

    tags = word_frequency.most_common(5)
    tags1 = []
    for tag in tags:
        tags1.append(tag[0])
    
    if (processed_data != []):
        return processed_data, tags1
    else:
        return 1, 1
