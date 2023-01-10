import data_processing as dp
import initialize as init
import numpy as np
import pandas as pd
from collections import Counter
from mlxtend.frequent_patterns import apriori, association_rules

def make_rules():
    Data, stop_words_array = init.readCSV()
    Data_list = Data['speech'].values.tolist()
    Data_length = len(Data_list)

    party_dict = {}
    speeches = []

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
            party = Data['political_party'][index]

            if (result != [] and type(party) == str):
                
                speeches.append(result)
                party_dict[id] = party
                id += 1

        index += 1    
        
        percentage = int(index/Data_length*100)
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage

    del Data_list

    print('Done!\nMaking Tags...\nProcessing: 0%')

    index = 0
    past_percentage = 0
    Data_length = len(speeches)
    useless_tags = ['κυριε', 'γιατι', 'προεδρε', 'υπαρχει', 'συναδελφοι', 'κυριοι', 'κυβερνηση', 'εδω', 'υπουργε', 'θεμα', 
    'δυο', 'πω', 'δηλαδη', 'νομοσχεδιο', 'ευχαριστω', 'κυριες', 'αφορα', 'χρονια', 'διοτι', 'πολιτικη', 'υπαρχουν', 'χωρα', 'αρθρο', 
    'γινει', 'θελω']
    tags_list = []
    columns = []

    for speech in speeches:
        speech_list = speech.split(' ')
        word_frequency = Counter(speech_list)
        
        tags = word_frequency.most_common(50)

        tags1 = []
        for tag in tags:
            if (tag[0] not in useless_tags):
                tags1.append(tag[0])
                if (tag[0] not in columns):
                    columns.append(tag[0])
        if (tags1 != []):        
            tags_list.append(tags1)

        percentage = int(index/Data_length*100)
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage
        index += 1

    del speech_list, word_frequency, tags, tags1

    print('Done!\nMaking DataFrame...\nProcessing: 0%')

    index = 0
    past_percentage = 0
    Data_length = len(tags_list)
    rows = []

    for word in columns:
        row = []
        for tags in tags_list:
            if word in tags:
                row.append(1)
            else:
                row.append(0)
        rows.append(row)

        percentage = int(index/Data_length*100)
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage

        index += 1

    tag_df = pd.DataFrame(rows, columns)
    print(tag_df)

    print('Done!\nMaking Rules...')
    frq_items = apriori(tag_df, min_support = 0.5, use_colnames = True)
    rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
    rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
    print(rules.head())

make_rules()