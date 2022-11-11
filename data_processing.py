import pandas as pd
from greek_stemmer import stemmer

def punctuation_removal(Data):
    preprocessed_speeches = []
    for index in Data.index:
        if Data['political_party'][index] != 'βουλη' and Data['political_party'][index] != 'μετωπο ευρωπαικης ρεαλιστικης ανυπακοης (μερα25)':
            speech = Data['speech'][index]
            preprocessed_speech = speech.replace(',',' ').replace('.',' ').replace('-',' ').replace('–',' ').replace(':', ' ').replace('«',' ').replace('»',' ').replace(';',' ').replace('!',' ').replace('\t',' ').replace('έ','ε').replace('ά','α').replace('ή','η').replace('ό','ο').replace('ύ','υ').replace('ί','ι').replace('ώ','ω').lower().split(' ')
            preprocessed_speech = [i for i in preprocessed_speech if i] 
            preprocessed_speeches.append(preprocessed_speech)
    return preprocessed_speeches

def stop_word_removal(preprocessed_speeches):
    preprocessed_speeches1 = []
    stop_words_array = []
    with open("stopwords.txt", "r", encoding="utf8") as file:
        for line in file.readlines():
            line = line[:-1]
            stop_words_array.append(line)
    for speech in preprocessed_speeches:
        for stopword in stop_words_array:
            speech = [word for word in speech if word != stopword]
        preprocessed_speeches1.append(speech)
    return preprocessed_speeches1

def stemming(preprocessed_speeches):
    preprocessed_speeches1 = []
    for speech in preprocessed_speeches:
        index = 0
        for word in speech:
            stemmed_word = stemmer.stem_word(word, 'VBG')
            if stemmed_word.islower():
                del speech[index]
            else:
                speech[index] = stemmed_word
            index += 1
        speech1 = " ".join(speech)   
        preprocessed_speeches1.append(speech1)
    return preprocessed_speeches1        

def makeMember_dicts(Data, preprocessed_speeches):
    member_dict_unprocessed = {}
    member_dict_processed = {}
    party_dict = {}
    index1 = 0
    for index in Data.index: 
        if Data['political_party'][index] != 'βουλη' and Data['political_party'][index] != 'μετωπο ευρωπαικης ρεαλιστικης ανυπακοης (μερα25)':
            key = Data['member_name'][index]
            if key in member_dict_unprocessed:
                list1 = member_dict_unprocessed[key]
                list1.append(Data['speech'][index])
                member_dict_unprocessed[key] = list1
                list2 = member_dict_processed[key]
                list2.append(preprocessed_speeches[index1])
                member_dict_processed[key] = list2    
            else:
                member_dict_unprocessed[key] = [Data['speech'][index]]
                member_dict_processed[key] = [preprocessed_speeches[index1]]
            index1 += 1    
            key = Data['political_party'][index]
            name = Data['member_name'][index]
            if key in party_dict:
                list = party_dict[key]
                if name not in list:
                    list.append(name)
                    party_dict[key] = list
            else:
                party_dict[key] = [name]

    return member_dict_unprocessed, member_dict_processed, party_dict        


Data = pd.read_csv('Greek_Parliament_Proceedings_1989_2020_DataSample.csv')

preprocessed_speeches1 = punctuation_removal(Data)
preprocessed_speeches2 = stop_word_removal(preprocessed_speeches1)
preprocessed_speeches_final = stemming(preprocessed_speeches2)

member_dict_unprocessed, member_dict_processed, party_dict = makeMember_dicts(Data, preprocessed_speeches_final)
#print(member_dict_processed['σκρεκας θεοδωρου κωνσταντινος'])