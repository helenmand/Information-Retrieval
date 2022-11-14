import pandas as pd
import data_processing as dp
import cos_similarity as cos_sim
import warnings
warnings.filterwarnings("ignore")

def init():
    Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020_DataSample.csv')  
    Data = Data_temp.loc[(Data_temp['political_party'] != 'βουλη') & (Data_temp['political_party'] != 'μετωπο ευρωπαικης ρεαλιστικης ανυπακοης (μερα25)')]
    Data.reset_index(drop=True, inplace=True)
    Data_list = Data['speech'].values.tolist()

    Docs = []
    tags_dict = {}
    member_dict = {}
    party_dict = {}
    id = 0
    for speech in Data_list:

        result = dp.process(speech)
        if (type(result) != int):
            Docs.append(result)
            tags_dict[id] = dp.makeTags(speech)

            name = Data['member_name'][id]
            if name in member_dict.keys():
                member_dict[name].append(id)
            else:
                member_dict[name] = [id]

            party = Data['political_party'][id]
            if party in party_dict.keys():
                if name not in party_dict[party]:
                    party_dict[party].append(name)
            else:
                party_dict[party] = [name]

            id += 1

        else:
            Data.drop([id], axis=0, inplace=True)
            Data.reset_index(drop=True, inplace=True)

    return Data, Docs, member_dict, party_dict, tags_dict 

Data, Docs, member_dict, party_dict, tags_dict = init()

query = dp.process('Τουρκία')
if (type(query) is int):
    print ('Bad query')

print(cos_sim.doc_query_similarity(Docs, query, len(Docs)))
#print(member_dict)
#print('--------------------------------------')
#print(party_dict)
#print('--------------------------------------')
#print(tags_dict)