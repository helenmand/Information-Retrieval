import query_similarity as cs

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
    return [[sitting_id] + get_sitting_info(sitting_id, Data, index_dict, tags_dict)[2::2] for sitting_id in member_dict[speaker]]

"""
Returns all the sittings by a party:

1. sitting ID
2. name of the speaker
3. tags - most frequent words in the speech
"""
def get_sittings_by_party(party, Data, index_dict, tags_dict, party_dict, member_dict):
    sittings = []
    for speaker in party_dict[party]:
        for sitting_id in member_dict[speaker]:
            sittings.append([sitting_id] + get_sitting_info(sitting_id, Data, index_dict, tags_dict)[0::4])
    return sittings

""" 
# for testing
if __name__ == "__main__":
    global Data, Docs, member_dict, party_dict, tags_dict
    Data, Docs, member_dict, party_dict, tags_dict = it.init()
    #sit = get_sittings_by_speaker('μπουκωρος γεωργιου χρηστος', Data, tags_dict, member_dict)
    #print(sit[0])
    #sit = get_sittings_by_party('νεα δημοκρατια', Data, tags_dict, party_dict)
    #print(sit[0:3])
"""
