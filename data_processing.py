from greek_stemmer import stemmer

def punctuation_removal(Data):
    preprocessed_data = []
    if (type(Data) is list):
        for line in Data:
            preprocessed_line = line.replace(',',' ').replace('.',' ').replace('-',' ').replace('–',' ').\
            replace(':', ' ').replace('«',' ').replace('»',' ').replace(';',' ').replace('!',' ').\
            replace('\t',' ').replace('έ','ε').replace('ά','α').replace('ή','η').replace('ό','ο').\
            replace('ύ','υ').replace('ί','ι').replace('ώ','ω').lower().split(' ')
            preprocessed_line = [i for i in preprocessed_line if i] 
            preprocessed_data.append(preprocessed_line)
    else:
        preprocessed_data = Data.replace(',', '').replace('.', '').replace('-', '').replace('–', '').\
        replace(':', '').replace('«', '').replace('»', '').replace(';', '').replace('!', '').\
        replace('\t', '').replace('έ','ε').replace('ά','α').replace('ή','η').replace('ό','ο').\
        replace('ύ','υ').replace('ί','ι').replace('ώ','ω').lower()
        preprocessed_data = [i for i in preprocessed_data if i]
        preprocessed_data = ''.join(preprocessed_data)
    return preprocessed_data

def stop_word_removal(preprocessed_data):
    preprocessed_data1 = []
    stop_words_array = []
    with open("stopwords.txt", "r", encoding="utf8") as file:
        for stopword in file.readlines():
            stopword = stopword[:-1]
            stop_words_array.append(stopword)
    if (type(preprocessed_data) is list):        
        for line in preprocessed_data:
            for stopword in stop_words_array:
                line = [word for word in line if word != stopword]
            preprocessed_data1.append(line)
    else:
        #temp_list = preprocessed_data.split(' ')
        #print(temp_list)
        #print(preprocessed_data)
        for stopword in stop_words_array:
            preprocessed_data1 = [word for word in preprocessed_data if word != stopword]
        print(preprocessed_data1)    
        preprocessed_data1 = ''.join(preprocessed_data)
        #print(preprocessed_data1)                        
    return preprocessed_data1

def stemming(preprocessed_data):
    preprocessed_data1 = []
    if (type(preprocessed_data) is list):
        for line in preprocessed_data:
            index = 0
            for word in line:
                stemmed_word = stemmer.stem_word(word, 'VBG')
                if stemmed_word.islower():
                    del line[index]
                else:
                    line[index] = stemmed_word
                index += 1
            line1 = " ".join(line)   
            preprocessed_data1.append(line1)
    else:
        index = 0
        if (" " in preprocessed_data):
            for word in preprocessed_data:
                stemmed_word = stemmer.stem_word(word, 'VBG')
                if stemmed_word.islower():
                    del preprocessed_data[index]
                else:
                    preprocessed_data[index] = stemmed_word
                index += 1
            preprocessed_data1 = " ".join(preprocessed_data)
        else:
            stemmed_word = stemmer.stem_word(preprocessed_data, 'VBG')
            if stemmed_word.islower():
                preprocessed_data1 = None
            else:
                preprocessed_data1 = [stemmed_word]          
    return preprocessed_data1            

def process(Data):
    preprocessed_data1 = punctuation_removal(Data)
    if preprocessed_data1 is None:
        return 1;
    preprocessed_data2 = stop_word_removal(preprocessed_data1)
    if preprocessed_data2 is None:
        return 1;
    preprocessed_data_final = stemming(preprocessed_data2)
    if preprocessed_data_final is None:
        return 1;

    return preprocessed_data_final