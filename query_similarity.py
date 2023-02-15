from math import log
from heapq import nsmallest
import numpy as np

"""
Returns the sim_dict dictionary containing the 5 most relevant speeches' ids (key) along with their rating (value)

Using the word dictionary, it calculates the tf_idf score of every document that contains at least one word that's contained in the query
The similarity formula is mentioned in the essay/report
"""
def doc_query_similarity(words_dict, query):
    index_dict = {}
    index = 0
    Tf_idf_dict = {}

    #Finds which documents are relevant
    Docs_To_Search = []
    for word in query:
        if word in words_dict:
            for id in words_dict[word]:
                if id not in index_dict:
                    Docs_To_Search.append(id)
                    Tf_idf_dict[id] = []
                    index_dict[index] = id
                    index += 1

    #For every word it calculates the docs' tf_idf score
    query_vector = []
    for word in query:
        if word in words_dict:
            
            #Idf calculation
            N = len(Tf_idf_dict) + 1
            Nt = len(words_dict[word]) + 1
            Idf = log(1 + N/Nt)

            #Query_vector Tf_Idf
            query_vector.append((1 + log(query.count(word))) * Idf)

            for id in Tf_idf_dict:
                if id not in words_dict[word]:

                    Tf_idf_dict[id].append(0.0)

                else:

                    #Tf calculation
                    Tf = 1 + log(words_dict[word][id])

                    #Tf_Idf calculation
                    Tf_idf_dict[id].append(Tf * Idf)

        else:

            query_vector.append((1 + log(query.count(word))) * log(2))
            for id in Tf_idf_dict:
                Tf_idf_dict[id].append(0.0)

    Docs_matrix = []
    for id in Tf_idf_dict:
        Docs_matrix.append(Tf_idf_dict[id])
    Docs_matrix = np.array(Docs_matrix)
    query_vector = np.array(query_vector)                

    #Calculates the similarity between the query and the docs
    similarity_dict = {}
    for i in range (0, len(Docs_matrix)-1):
       
        if (len(Docs_matrix[i]) > 1):
            sim_value = sum(Docs_matrix[i])/(np.linalg.norm(Docs_matrix[i]) * np.linalg.norm(query_vector))
        else:
            sim_value = sum(Docs_matrix[i])
        similarity_dict[index_dict[i]] = sim_value

    #Sorting
    heap = [(-value, key) for key, value in similarity_dict.items()]
    sim_list = nsmallest(5, heap)

    sim_dict = {}
    for tuple in sim_list:
        sim_dict[tuple[1]] = -1 * tuple[0]

    return sim_dict   