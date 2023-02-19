import pandas as pd
import data_processing as dp
import warnings

warnings.filterwarnings("ignore")

"""
Returns two lists: The first is a dataframe containing the content of the CSV file without including the political party 'βουλη' (useless data) 
                    and the second contains the stop words from the stopwords.txt file.
"""
def readCSV():
    print("Reading CSV and StopWords file...")
    Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020.csv')
    Data = Data_temp.loc[(Data_temp['political_party'] != 'βουλη')]
    Data.reset_index(drop=True, inplace=True)

    stop_words_array = []
    with open(".\\app_files\stopwords.txt", "r", encoding="utf8") as file:
        for stopword in file.readlines():
            stopword = stopword[:-1]
            stop_words_array.append(stopword)
    print('Done!')
    return Data, stop_words_array 

"""
Returns:
1. Data: a dataframe given by the readCSV() function
2. index_dict: dictionary (key: id, meaning the processed speech's identification number, value: index of said speech in the Data dataframe)
3. words_dict: term frequency dictionary (key: word, meaning any string that's in a processed speech, value: id which in turn is a key for the value of the frequency of said word)
4. stop_words_array: list given by the readCSV() function
5. member_dict: parliament member dictionary (key: member name, value: list of ids of his/her processed speeches)
6. party_dict: parliament party dictionary (key: party name, value: list of party's members' names)
7. tags_dict: dictionary (key: id, value: a list containing the 5 most frequent words of the id'd speech)

This function calculates all necessary information for the app to be able to perform queries using the data_processing script
Not all speeches are processed: If speeches are skipped because of the increment, are less or equal to 100 words, contain only stop words
                                or don't have a speaker or party documented then they won't be on the final database
"""
def init():
    Data, stop_words_array = readCSV()
    Data_list = Data['speech'].values.tolist()
    Data_length = len(Data_list)

    index_dict = {}
    words_dict = {}
    tags_dict = {}
    member_dict = {}
    party_dict = {}

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

    #t0 = time.time()
    print ('Processing: 0%')
    for speech in Data_list:

        name = Data['member_name'][index]
        party = Data['political_party'][index]
        speech_list = speech.split(' ')
        if (len(speech_list) > 100 and index%increment == 0 and type(name) == str and type(party) == str):
            result, tags = dp.process(speech, stop_words_array)

            if (type(result) != int):

                index_dict[id] = index

                for word in result:
                    if word in words_dict:
                        if id in words_dict[word]:
                            words_dict[word][id] += 1
                        else:
                            words_dict[word][id] = 1
                    else:
                        words_dict[word] = {}
                        words_dict[word][id] = 1
            
                tags_dict[id] = tags

                if name in member_dict:
                    member_dict[name].append(id)
                else:
                    member_dict[name] = [id]

                if party in party_dict:
                    if name not in party_dict[party]:
                        party_dict[party].append(name)
                else:
                    party_dict[party] = [name]
            
                id += 1

        index += 1    

        percentage = int(index/Data_length*100)
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage

    print('Done!')
    return Data, index_dict, words_dict, stop_words_array, member_dict, party_dict, tags_dict 