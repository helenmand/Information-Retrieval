import data_processing as dp
import initialize as init
from collections import Counter

"""
Makes 2 .txt files for keywords by member and by party (on ascending order from oldest date to newest)

Uses the term frequency to determine importance
"""
def find_KeyWords():
    Data, stop_words_array = init.readCSV()
    Data_list = Data['speech'].values.tolist()
    Data_length = len(Data_list)

    date_dict_member = {}
    date_dict_party = {}

    past_percentage = 0
    index = 0
    id = 0

    #CHANGE THIS VARIABLE TO MODIFY THE AMOUNT OF DATA THAT'LL BE PROCESSED (HIGHER == LESS DATA, ALL DATA == 1)
    ################################
    increment = 5
    ################################

    if (increment <= 0):
        print('Increment can\'t be less than 1. (Set automatically to 1)')
        increment = 1

    #Processes the speeches(without stemming) and makes dictionaries based on the dates for the members and parties
    print ('Processing: 0%')
    for speech in Data_list:

        speech_list = speech.split(' ')
        if (len(speech_list) > 100 and index%increment == 0):
            result = dp.preprocess(speech, stop_words_array)
            name = Data['member_name'][index]
            party = Data['political_party'][index]

            if (result != [] and type(name) == str and type(party) == str):
                
                date_temp = Data['sitting_date'][index]
                date = date_temp[-4:]
                
                if date in date_dict_member:
                    if name in date_dict_member[date]:
                        date_dict_member[date][name] = date_dict_member[date][name] + ' ' + result
                    else:
                        date_dict_member[date][name] = result
                else:
                    date_dict_member[date] = {name:result}

                if date in date_dict_party:
                    if party in date_dict_party[date]:
                        date_dict_party[date][party] = date_dict_party[date][party] + ' ' + result
                    else:
                        date_dict_party[date][party] = result
                else:
                    date_dict_party[date] = {party:result}
            
                id += 1

        index += 1    
        
        percentage = int(index/Data_length*100)
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage

    print('Done!')

    #Makes the first file, writing the 15 most frequent terms (key words) said by the members sorted by the sitting date
    file = open(".\\generated_files\MemberKeyWords.txt", "w", encoding="utf-8")
    for date in date_dict_member:
        file.write('Year: ' + str(date) + '\n============================\n============================\n')
        for name in date_dict_member[date]:
            file.write(name + ':\n')
            dict_list = date_dict_member[date][name].split(' ')
            word_frequency = Counter(dict_list)

            tags = word_frequency.most_common(15)
            tags1 = []
            for tag in tags:
                 tags1.append(tag[0])
            file.write(', '.join(tags1))
            file.write('\n-------------\n')
    
    file.close()

    #Makes the first file, writing the 15 most frequent terms (key words) said by the parties sorted by the sitting date
    file1 = open(".\\generated_files\PartyKeyWords.txt", "w", encoding="utf-8")
    for date in date_dict_party:
        file1.write('Year: ' + str(date) + '\n============================\n============================\n')
        for party in date_dict_party[date]:
            file1.write(party + ':\n')
            dict_list = date_dict_party[date][party].split(' ')
            word_frequency = Counter(dict_list)

            tags = word_frequency.most_common(15)
            tags1 = []
            for tag in tags:
                tags1.append(tag[0])
            file1.write(', '.join(tags1))
            file1.write('\n-------------\n')

    file1.close()
    print('\nFiles made!')

##################################
##################################
find_KeyWords()