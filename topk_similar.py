import data_processing as dp
import initialize as init
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""
Makes a file with the top k similar speakers

Uses cosine similarity
"""
def topk_similar(k):
    Data, stop_words_array = init.readCSV()
    Data_list = Data['speech'].values.tolist()
    Data_length = len(Data_list)

    member_dict = {}
    party_dict = {}
    Docs = {}

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

    #Processes the speeches and makes dictionaries for the final Docs, members and parties
    print ('Processing: 0%')
    for speech in Data_list:

        speech_list = speech.split(' ')
        if (len(speech_list) > 100 and index%increment == 0):
            result, tags = dp.process(speech, stop_words_array)
            name = Data['member_name'][index]

            if (type(result) != int and type(name) == str):
                
                if name in member_dict.values():
                    index_id = list(member_dict.keys())[list(member_dict.values()).index(name)]
                    Docs[index_id] = Docs[index_id] + ' ' + ' '.join(result)
                else:
                    Docs[id] = ' '.join(result)
                    member_dict[id] = name
                    party_dict[name] = Data['political_party'][index]
                    id += 1
        
        index += 1    
        
        percentage = int(index/Data_length*100)
        if (past_percentage != percentage):
            print('Processing: ' + str(percentage) + '%')
            past_percentage = percentage

    print('Done!')

    #Uses tf_idf and cosine similarity for the similarity calculation
    print('Calculating Similarity...')
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(list(Docs.values()))
    tfidf_matrix = tfidf_matrix.toarray()
    similarity_matrix = cosine_similarity(tfidf_matrix[:], tfidf_matrix)

    #Finds k most similar based on their cos similarity
    topk_list = []
    topk_values = []
    for i in range(k):
        topk_list.append(0)
        topk_values.append(0)
    for i in range(len(similarity_matrix)):
        for j in range(len(similarity_matrix)):
            inserted = False
            if (i != j and [j, i] not in topk_list):
                for r in range(k):

                    if (not inserted and similarity_matrix[i][j] > topk_values[r]):
                        inserted = True
                        pos = r
                    elif (inserted):
                        temp = topk_list[pos]
                        topk_list[pos] = topk_list[r]
                        topk_list[r] = temp

                        temp1 = topk_values[pos]
                        topk_values[pos] = topk_values[r]
                        topk_values[r] = temp1
                if (inserted):
                    topk_list[pos] = [i, j]
                    topk_values[pos] = similarity_matrix[i][j]
    
    #Makes the file 
    file = open(".\generated_files\TopK_Similar.txt", "w", encoding="utf-8")
    file.write('\n===============\nTop ' + str(k) + ' pairs:\n===============\n\n')
    counter = 0
    for pair in topk_list:
        file.write(member_dict[pair[0]] + ' (' + str(party_dict[member_dict[pair[0]]]) + ') ------- ' + 
        member_dict[pair[1]] + ' (' + str(party_dict[member_dict[pair[1]]]) + ')  (Score: ' + str(topk_values[counter]) + ')\n\n')
        counter += 1
    file.close()
    print('File made!')

###############################
###############################
topk_similar(10)