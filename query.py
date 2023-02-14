import query_similarity as cs
import initialize as it
import random as rand

"""
Returns the 5 most similar documents (sittings) to a query:

1. sitting ID
2. name of the speaker
3. political party of the speaker
4. tags - most frequent words in the speech
"""
def get_sittings(query, Data, index_dict, words_dict, tags_dict):
    similarities = cs.doc_query_similarity(words_dict, query)
    
    sittings = []
    for sitting in similarities:
        data = [item for sublist in Data.iloc[[index_dict[sitting]], [0, 5]].values.tolist() for item in sublist]

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
def get_sitting_info(sitting_id, Data, index_dict, tags_dict):
    data = [item for sublist in Data.iloc[[index_dict[int(sitting_id)]], [0, 1, 5, 10] ].values.tolist() for item in sublist]
    
    return data + [' '.join(tags_dict.get(int(sitting_id)))]

"""
Returns all the sittings by a speaker:

1. sitting ID
2. political party of the speaker
3. tags - most frequent words in the speech
"""
def get_sittings_by_speaker(speaker, Data, index_dict, tags_dict, member_dict):
    sittings =  [[sitting_id] + get_sitting_info(sitting_id, Data, index_dict, tags_dict)[2::2] for sitting_id in member_dict[speaker]]
    return sittings[::-1]

"""
Returns 5 sittings by a party, each sitting is by a different member:

1. sitting ID
2. name of the speaker
3. tags - most frequent words in the speech
"""
def get_sittings_by_party(party, Data, index_dict, tags_dict, party_dict, member_dict):
    sittings = []
    max_speakers = 5 if len(party_dict[party])>5 else len(party_dict[party])
    for speaker in party_dict[party][:max_speakers]:
        for sitting_id in member_dict[speaker]:
            sittings.append([sitting_id] + get_sitting_info(sitting_id, Data, index_dict, tags_dict)[0::4])
            break
    return sittings[::-1]


"""# for testing
if __name__ == "__main__":
    global Data, member_dict, party_dict, tags_dict
    Data, Docs, index_dict, words_dict, stop_words_array, member_dict, party_dict, tags_dict = it.init()
    
    #sit = get_sittings_by_speaker(speaker='αραμπατζη αθανασιου φωτεινη',Data=Data,index_dict=index_dict, tags_dict=tags_dict, member_dict=member_dict)
   # print(sit[::-1])
    sit = get_sittings_by_party(party='νεα δημοκρατια',Data=Data, index_dict=index_dict, tags_dict=tags_dict, party_dict=party_dict, member_dict=member_dict)
    print(len(sit))
"""