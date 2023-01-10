import data_processing as dp
import initialize as init
import pandas as pd
from collections import Counter
from mlxtend.frequent_patterns import apriori, association_rules

def make_rules(start_year = 'None', end_year = 'None', pref_speaker = 'None', pref_party = 'None', pref_word = 'None', user_useless_tags = [], minimum_support = 0.03):
    Data, stop_words_array = init.readCSV()
    Data_list = Data['speech'].values.tolist()
    Data_length = len(Data_list)

    speeches = []

    past_percentage = 0
    index = 0

    #CHANGE THIS VARIABLE TO MODIFY THE AMOUNT OF DATA THAT'LL BE PROCESSED (HIGHER = LESS DATA)
    ################################
    increment = 5
    ################################

    if (increment <= 0):
        print('Are you stupid? :3')
        increment = 1

    print ('Processing: 0%')
    for speech in Data_list:

        date_temp = Data['sitting_date'][index]
        year = date_temp[-4:]
        party = Data['political_party'][index]
        speaker = Data['member_name'][index]

        if ((year >= start_year or start_year == 'None') and (year <= end_year or end_year == 'None') and (speaker == pref_speaker or pref_speaker == 'None') and (party == pref_party or pref_party == 'None')):
            speech_list = speech.split(' ')
            if (len(speech_list) > 100 and index%increment == 0):
                result = dp.preprocess(speech, stop_words_array)
                party = Data['political_party'][index]

                if (result != [] and (pref_word in result or pref_word == 'None')):
                    speeches.append(result)

        index += 1    
        
        percentage = int(index/Data_length*100)
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage

    if not any(speeches):
        print('No suitable speeches found!')
        return 1

    print('Done!\nMaking Tags...\nProcessing: 0%')

    index = 0
    past_percentage = 0
    Data_length = len(speeches)
    useless_tags = ['κυριε', 'γιατι', 'προεδρε', 'υπαρχει', 'συναδελφοι', 'κυριοι', 'εδω', 'υπουργε', 'θεμα', 
    'δυο', 'πω', 'δηλαδη', 'ευχαριστω', 'κυριες', 'αφορα', 'χρονια', 'διοτι', 'πολιτικη', 'υπαρχουν', 'χωρα', 'αρθρο', 
    'γινει', 'θελω', 'βεβαιως', 'κανει', 'νομιζω', 'σο', 'πα', 'ερωτηση']
    tags_list = []
    column_names = []

    for speech in speeches:
        speech_list = speech.split(' ')
        word_frequency = Counter(speech_list)
        
        tags = word_frequency.most_common(50)

        tags1 = []
        for tag in tags:
            if (tag[0] not in useless_tags and tag[0] not in user_useless_tags):
                tags1.append(tag[0])
                if (tag[0] not in column_names):
                    column_names.append(tag[0])
        if (tags1 != []):        
            tags_list.append(tags1)

        percentage = int(index/Data_length*100) + 1
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage
        index += 1

    if not any(tags_list):
        print('Couldn\'t find good tags!')
        return 1

    print('Done!\nMaking DataFrame...\nProcessing: 0%')

    index = 0
    past_percentage = 0
    Data_length = len(column_names)
    df_dict = {}

    for word in column_names:
        column = []
        for tags in tags_list:
            if word in tags:
                column.append(True)
            else:
                column.append(False)
        df_dict[word] = column

        percentage = int(index/Data_length*100) + 1
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage

        index += 1

    tag_df = pd.DataFrame(df_dict)

    print('Done!\nMaking Rules...')

    frequent_items = apriori(tag_df, min_support = minimum_support, use_colnames = True)

    if frequent_items.empty:
        print('Couldn\'t find frequent sets (minimum support is too high?)')
        return 1

    rules = association_rules(frequent_items, metric ="lift", min_threshold = 1)
    rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])

    file = open("Rules.txt", "w", encoding="utf-8")
    if (start_year != 'None'):
        file.write('From: ' + start_year + '\n')
    if (end_year != 'None'):
        file.write('Until: ' + start_year + '\n')
    if (pref_party != 'None'):
        file.write('Party: ' + pref_party + '\n')
    if (pref_speaker != 'None'):
        file.write('Speaker: ' + pref_speaker + '\n')
    if (pref_word != 'None'):
        file.write('Key word: ' + pref_word + '\n')
    file.write('===================================================================================================================================================\n')
    for index, row in rules.iterrows():
        if (pref_word == 'None' or pref_word in row['antecedents'] or pref_word in row['consequents']):
            antecedents = '(' + ', '.join(row['antecedents']) + ')'
            consequents = '(' + ', '.join(row['consequents']) + ')'
            file.write(antecedents + '  -------->  ' + consequents + '   Support: ' + str(row['support']) + ', Confidence: ' + str(row['confidence']) + '\n')

    file.write('===================================================================================================================================================')
    file.close()

    print('File made!')

##################################################################################
##################################################################################
make_rules('None', 'None', 'μητσοτακης κωνσταντινου κυριακος', 'None', 'τσιπρα', [], 0.04)