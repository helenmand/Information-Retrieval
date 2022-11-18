import pandas as pd
import data_processing as dp
import cos_similarity as cos_sim
import warnings
import time

warnings.filterwarnings("ignore")

def init():
    print("Reading CSV and StopWords file...")
    #Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020_DataSample.csv')
    Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020.csv')
    Data = Data_temp.loc[(Data_temp['political_party'] != 'βουλη')]
    Data.reset_index(drop=True, inplace=True)
    Data_list = Data['speech'].values.tolist()
    Data_length = len(Data_list)
    print('Done!')

    Docs = []
    index_dict = {}
    words_dict = {}
    tags_dict = {}
    member_dict = {}
    party_dict = {}

    past_percentage = 0
    index = 0
    id = 0

    stop_words_array = []
    with open("stopwords.txt", "r", encoding="utf8") as file:
        for stopword in file.readlines():
            stopword = stopword[:-1]
            stop_words_array.append(stopword)

    t0 = time.time()
    print ('Processing: 0%')
    for speech in Data_list:

        speech_list = speech.split(' ')
        if (len(speech_list) > 15):
            result, tags = dp.process(speech, stop_words_array)

            if (type(result) != int):

                index_dict[id] = index

                for word in result:
                    if word in words_dict:
                        if id in words_dict[word]:
                            words_dict[word][id] += 1
                        else:
                            words_dict[word][id] = 1
                    else:
                        words_dict[word] = {}
                        words_dict[word][id] = 1
            
                tags_dict[id] = tags
                Docs.append(' '.join(result))
            
                name = Data['member_name'][id]
                if name in member_dict:
                    member_dict[name].append(id)
                else:
                    member_dict[name] = [id]

                party = Data['political_party'][id]
                if party in party_dict:
                    if name not in party_dict[party]:
                        party_dict[party].append(name)
                else:
                    party_dict[party] = [name]
            
                id += 1

        index += 1    

        percentage = int(index/Data_length*100)
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            print (time.time() - t0)
            t0 = time.time()
            past_percentage = percentage

    print('Done!')
    return Data, Docs, index_dict, words_dict, stop_words_array, member_dict, party_dict, tags_dict 

#if __name__ == "__main__":
    #Data, Docs, member_dict, party_dict, tags_dict = init()

'''
Data, Docs, words_dict, stop_words_array, member_dict, party_dict, tags_dict = init()

query, query_tags = dp.process('Αγρότης', stop_words_array)
if (type(query) is int):
    print ('Bad query')

#print(len(words_dict.keys()))
print(cos_sim.doc_query_similarity(Docs, words_dict, query))
'''