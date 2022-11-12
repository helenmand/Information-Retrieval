def makeDicts(Data, preprocessed_speeches):
    member_dict_unprocessed = {}
    member_dict_processed = {}
    party_dict = {}
    index1 = 0
    for index in Data.index: 
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