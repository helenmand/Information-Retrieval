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

    Docs.append(query)
    tfidf_vector = tfidf_vectorizer.fit_transform(Docs)
    Docs_matrix = tfidf_vector.toarray()
    query_vector = Docs_matrix[len(Docs)-1, :]

    similarity_dict = {}
    for i in range (0, numOfDocs-1):
        sim_value = cosine_similarity([query_vector], [Docs_matrix[i,:]])
        similarity_dict[i] = sim_value[0][0]

    heap = [(-value, key) for key, value in similarity_dict.items()]
    sim_list = nsmallest(5, heap)

    sim_dict = {}
    for tuple in sim_list:
        sim_dict[tuple[1]] = -1 * tuple[0]

    return sim_dict   