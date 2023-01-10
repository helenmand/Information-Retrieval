import data_processing as dp
import initialize as init
from collections import Counter

def find_KeyWords():
    Data, stop_words_array = init.readCSV()
    Data_list = Data['speech'].values.tolist()
    Data_length = len(Data_list)

    date_dict_member = {}
    date_dict_party = {}

    past_percentage = 0
    index = 0
    id = 0

    #CHANGE THIS VARIABLE TO MODIFY THE AMOUNT OF DATA THAT'LL BE PROCESSED (HIGHER = LESS DATA)
    ################################
    increment = 5
    ################################

    if (increment <= 0):
        print('Are you stupid? :3')
        increment = 1

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

    file = open("MemberKeyWords.txt", "w", encoding="utf-8")
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

    file1 = open("PartyKeyWords.txt", "w", encoding="utf-8")
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