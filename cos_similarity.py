from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from math import log
from heapq import nsmallest
import numpy as np

def doc_doc_similarity(Docs):
    tfidf_vectorizer = TfidfVectorizer()

    tfidf_matrix = tfidf_vectorizer.fit_transform(Docs)
    ddsim_matrix = cosine_similarity(tfidf_matrix[:], tfidf_matrix)

    return ddsim_matrix

def doc_query_similarity(Docs, index_dict, words_dict, query):
    index_dict = {}
    index = 0
    Tf_idf_dict = {}

    #query1 = query.split(' ')
    for word in query:
        if word in words_dict:
            for id in words_dict[word]:
                if id not in Tf_idf_dict:
                    Tf_idf_dict[id] = []
                    index_dict[index] = id
                    index += 1

    query_vector = []
    for word in query:
        if word in words_dict:
            
            #Idf calculation
            N = len(Tf_idf_dict) + 1
            Nt = len(words_dict[word]) + 1
            Idf = log(N/(Nt + 1))

            #Query_vector Tf_Idf
            query_vector.append((query.count(word)/len(query)) * Idf)

            for id in Tf_idf_dict:
                if id not in words_dict[word]:

                    Tf_idf_dict[id].append(0.0)

                else:

                    #Tf calculation
                    Tf = words_dict[word][id]/len((Docs[index_dict[id]].split(' ')))

                    #Tf_Idf calculation
                    Tf_idf_dict[id].append(Tf * Idf)

        else:

            query_vector.append(query.count(word)/len(query) * log((len(Tf_idf_dict) + 1)/2))
            for id in Tf_idf_dict:
                Tf_idf_dict[id].append(0.0)

    Docs_matrix = []
    for id in Tf_idf_dict:
        Docs_matrix.append(Tf_idf_dict[id])
    Docs_matrix = np.array(Docs_matrix)                

    similarity_dict = {}
    for i in range (0, len(Docs_matrix)-1):
        sim_value = ((np.dot(query_vector, Docs_matrix[i]))/(len(query_vector) * 2))
        similarity_dict[index_dict[i]] = sim_value

    heap = [(-value, key) for key, value in similarity_dict.items()]
    sim_list = nsmallest(5, heap)

    sim_dict = {}
    for tuple in sim_list:
        sim_dict[tuple[1]] = -1 * tuple[0]

    return sim_dict   