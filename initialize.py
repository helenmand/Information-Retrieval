import pandas as pd
import data_processing as dp
import cos_similarity as cos_sim
import warnings

warnings.filterwarnings("ignore")

def init():
    #Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020_DataSample.csv')
    Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020.csv')
    Data = Data_temp.loc[(Data_temp['political_party'] != 'βουλη')]
    Data.reset_index(drop=True, inplace=True)
    Data_list = Data['speech'].values.tolist()

    Docs = []
    words_dict = {}
    tags_dict = {}
    member_dict = {}
    party_dict = {}
    past_percentage = 0
    id = 0

    stop_words_array = []
    with open("stopwords.txt", "r", encoding="utf8") as file:
        for stopword in file.readlines():
            stopword = stopword[:-1]
            stop_words_array.append(stopword)

    print ('0%')
    for speech in Data_list:
        result, tags = dp.process(speech, stop_words_array)
        if (type(result) != int):

            for word in result:
                if word in words_dict:
                    words_dict[word].append(id)
                else:
                    words_dict[word] = [id]
            
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

        else:
            Data.drop([id], axis=0, inplace=True)
            Data.reset_index(drop=True, inplace=True)
        print (len(words_dict))
        percentage = int(id/len(Data.index)*100)
        if (past_percentage != percentage):
            print(str(percentage) + '%')
            past_percentage = percentage

    return Data, Docs, words_dict, stop_words_array, tags_dict 

#if __name__ == "__main__":
    #Data, Docs, member_dict, party_dict, tags_dict = init()

#Data, Docs, words_dict, stop_words_array, member_dict, party_dict, tags_dict = init()
'''
query, query_tags = dp.process('Αγρότης', stop_words_array)
if (type(query) is int):
    print ('Bad query')

#print(len(words_dict.keys()))
print(cos_sim.doc_query_similarity(Docs, words_dict, query))
'''