import cos_similarity as cs

"""
Returns the 5 most similar documents (sittings) to a query:

1. sitting ID
2. name of the speaker
3. political party of the speaker
4. tags - most frequent words in the speech
"""
def get_sittings(query, Data, Docs, index_dict, words_dict, tags_dict):
    similarities = cs.doc_query_similarity(Docs, index_dict, words_dict, query)
    
    sittings = []
    for sitting in similarities:
        data = [item for sublist in Data.iloc[[sitting], [0, 5]].values.tolist() for item in sublist]

        sittings.append([sitting] + data + [' '.join(tags_dict.get(sitting))] + [similarities[sitting]])
    
    return sittings

"""
Returns information about a specific sitting:

1. name of the speaker
2. date the sitting took place
3. political party of the speaker
4. speech 
5. tags - most frequent words in the speech
"""
def get_sitting_info(sitting_id, Data, tags_dict):
    data = [item for sublist in Data.iloc[[int(sitting_id)], [0, 1, 5, 10] ].values.tolist() for item in sublist]
    
    return data + [' '.join(tags_dict.get(int(sitting_id)))]

"""
Returns all the sittings by a speaker:

1. sitting ID
2. political party of the speaker
3. tags - most frequent words in the speech
"""
def get_sittings_by_speaker(speaker, Data, tags_dict, member_dict):
    return [[sitting_id] + get_sitting_info(sitting_id, Data, tags_dict)[2::2] for sitting_id in member_dict[speaker]]

"""
Returns all the sittings by a party:

1. sitting ID
2. name of the speaker
3. tags - most frequent words in the speech
"""
def get_sittings_by_party(party, Data, tags_dict, party_dict, member_dict):
    sittings = []
    for speaker in party_dict[party]:
        for sitting_id in member_dict[speaker]:
            sittings.append([sitting_id] + get_sitting_info(sitting_id, Data, tags_dict)[0::4])
    return sittings


""" 
# dummy functions 
import csv
import random
import string
import initialize as it

def clean_tags(text):
    speech_sample = [random.choice(text.split(' ')) for _ in range(0,5)]
    speech_sample = (' '.join(speech_sample)).translate(str.maketrans('', '', string.punctuation))
    return speech_sample

def get_random_data():
    sittings = []
    # 0:'member_name', 1:'sitting_date', 'parliamentary_period', 'parliamentary_session', 4:'parliamentary_sitting', 
    # 5: 'political_party', 'government', 'member_region', 'roles', 'member_gender', 'speech
    with open('Greek_Parliament_Proceedings_1989_2020_DataSample.csv','r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            speech_sample = clean_tags(row[10])
            sittings.append([row[4], row[0], row[5], speech_sample, random.randint(0,100)/100])
    
    sample = random.sample(sittings, 5)
    for i in range(0,5):
        sample[i].insert(0, i)

    return sample

def sittings_by_speaker(speaker):
    sittings = []
    with open('Greek_Parliament_Proceedings_1989_2020_DataSample.csv','r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0].lower() == speaker:
                speech_sample = clean_tags(row[10])
                sittings.append([row[4], row[5], speech_sample])
        return sittings

def sittings_by_party(party):
    sittings = []
    with open('Greek_Parliament_Proceedings_1989_2020_DataSample.csv','r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[5].lower() == party:
                speech_sample = clean_tags(row[10])
                sittings.append([row[4], row[0], speech_sample])
        return sittings

if __name__ == "__main__":
    global Data, Docs, member_dict, party_dict, tags_dict
    Data, Docs, member_dict, party_dict, tags_dict = it.init()
    #sit = get_sittings_by_speaker('μπουκωρος γεωργιου χρηστος', Data, tags_dict, member_dict)
    #print(sit[0])
    #sit = get_sittings_by_party('νεα δημοκρατια', Data, tags_dict, party_dict)
    #print(sit[0:3])
"""
