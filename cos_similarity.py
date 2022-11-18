from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from heapq import nsmallest

def doc_doc_similarity(Docs):
    tfidf_vectorizer = TfidfVectorizer()

    tfidf_matrix = tfidf_vectorizer.fit_transform(Docs)
    ddsim_matrix = cosine_similarity(tfidf_matrix[:], tfidf_matrix)

    return ddsim_matrix

def doc_query_similarity(Docs, words_dict, query):
    tfidf_vectorizer = TfidfVectorizer()

    index_dict = {}
    index = 0
    Docs_To_Search = []
    query1 = query.split(' ')
    for word in query1:
        if word in words_dict:
            for id in words_dict[word]:
                if id not in Docs_To_Search:
                    index_dict[index] = id
                    index += 1
                    Docs_To_Search.append(Docs[id])
    
    Docs_To_Search.append(query)
    tfidf_vector = tfidf_vectorizer.fit_transform(Docs_To_Search)
    Docs_matrix = tfidf_vector.toarray()
    query_vector = Docs_matrix[len(Docs_To_Search)-1, :]

    similarity_dict = {}
    for i in range (0, len(Docs_To_Search)-2):
        sim_value = cosine_similarity([query_vector], [Docs_matrix[i,:]])
        similarity_dict[index_dict[i]] = sim_value[0][0]

    heap = [(-value, key) for key, value in similarity_dict.items()]
    sim_list = nsmallest(5, heap)

    sim_dict = {}
    for tuple in sim_list:
        sim_dict[tuple[1]] = -1 * tuple[0]

    return sim_dict   