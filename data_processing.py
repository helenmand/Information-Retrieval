from greek_stemmer import stemmer
from collections import Counter

"""
Returns a list of the Data string with no punctuation and replacing most special characters
"""
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

"""
Returns a joined string of a list of words after removing the stop words from it
"""
def stop_word_removal(preprocessed_data, stop_words_array):
    preprocessed_data1 = []
    for word in preprocessed_data:
        if word not in stop_words_array:
            preprocessed_data1.append(word)
    preprocessed_data1 = ' '.join(preprocessed_data1)                          
    return preprocessed_data1

"""
Returns a list from a string after stemming the words in it
"""
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

"""
Returns a string after undergoing processing by removing its punctuation and stop words
"""
def preprocess(Data, stop_words_array):
    preprocessed_data = stop_word_removal(punctuation_removal(Data), stop_words_array)
    return preprocessed_data

"""
Returns:
1. processed_data: a list formed after the Data(speech) list underwent the preprocessing and stemming procedures. Checks if it's empty before returning
2. tags1: Most common terms in the preprocessed Data(speech)
"""
def process(Data, stop_words_array):

    preprocessed_data = preprocess(Data, stop_words_array)
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
