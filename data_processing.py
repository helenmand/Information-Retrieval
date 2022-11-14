from greek_stemmer import stemmer
import collections
from heapq import nsmallest

def punctuation_removal(Data):
    preprocessed_data = []
    preprocessed_data = Data.replace(',', ' ').replace('.', ' ').replace('-', ' ').replace('–', ' ').\
    replace(':', ' ').replace('«', ' ').replace('»', ' ').replace(';', ' ').replace('!', ' ').replace('…',' ').\
    replace('\t', ' ').replace('έ','ε').replace('ά','α').replace('ή','η').replace('ό','ο').\
    replace('ύ','υ').replace('ί','ι').replace('ώ','ω').replace('Ό','ο').replace('Έ','ε').replace('Ά','α').replace('Ή','η').\
    replace('Ύ','υ').replace('Ί','ι').replace('Ώ','ω').lower()
    preprocessed_data = preprocessed_data.split(' ')
    preprocessed_data = [word for word in preprocessed_data if word != '']
    return preprocessed_data

def stop_word_removal(preprocessed_data):
    preprocessed_data1 = []
    stop_words_array = []
    with open("stopwords.txt", "r", encoding="utf8") as file:
        for stopword in file.readlines():
            stopword = stopword[:-1]
            stop_words_array.append(stopword)
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
    preprocessed_data1 = ' '.join(preprocessed_data)        
    return preprocessed_data1            

def process(Data):

    preprocessed_data1 = punctuation_removal(Data)
    preprocessed_data2 = stop_word_removal(preprocessed_data1)
    preprocessed_data_final = stemming(preprocessed_data2)

    try:
        if (preprocessed_data_final != ''):
            return preprocessed_data_final
        else:
            return 1
    except:
        print (Data)
        print (preprocessed_data1)
        print (preprocessed_data2)
        print (preprocessed_data_final) 

def makeTags(Data):

    preprocessed_data1 = punctuation_removal(Data)
    preprocessed_data2 = stop_word_removal(preprocessed_data1)

    data_list = preprocessed_data2.split(' ')
    word_frequency = collections.Counter(data_list)

    tf_dict = {}
    for word in word_frequency.keys():
        if word.isalpha():
            tf_dict[word] = word_frequency[word] / len(Data)

    heap = [(-value, key) for key, value in tf_dict.items()]
    tf_list = nsmallest(5, heap)

    tags = []
    for tuple in tf_list:
        tags.append(tuple[1])

    return tags
