import data_processing as dp
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from heapq import nsmallest

def doc_doc_similarity(Docs):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(Docs)
    ddsim_matrix = cosine_similarity(tfidf_matrix[:], tfidf_matrix)
    return ddsim_matrix

def doc_query_similarity(Docs, query, numOfDocs):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(Docs)
    tfidf_query = tfidf_vectorizer.fit_transform(query)
    similarity_dict = []
    id = 0
    for i in range (0, numOfDocs):
        sim_value = cosine_similarity(tfidf_query, tfidf_matrix[i,:])
        similarity_dict[id] = sim_value
        heap = [(-value, key) for key, value in similarity_dict.items()]
        id += 1
    return nsmallest(5, heap)    
            


Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020_DataSample.csv')  
Data = Data_temp.loc[(Data_temp['political_party'] != 'βουλη') & (Data_temp['political_party'] != 'μετωπο ευρωπαικης ρεαλιστικης ανυπακοης (μερα25)')]
Data.reset_index(drop=True, inplace=True)
Data_list = Data['speech'].values.tolist()
Docs = dp.process(Data_list)
query = dp.process('Οι Αγρότες.!')
print (query)
if (Docs == 1):
    print('wtf')
else:
    similar = doc_query_similarity(Docs, query, len(Docs))
    print (similar)
#print(Data)
#print(len(matrix[0]))    
#print (Data['speech'][len(matrix[0])-2])
#print('-----------------------------------------------')
#print(Data['speech'][len(matrix[0])-3])    