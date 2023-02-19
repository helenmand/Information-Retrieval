import data_processing as dp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import data_processing as dp
import initialize as init

"""
Performs LSI on the sittings in order to extract topics. 
The number of topics was extracted by studying the topic number - strength plot.   
"""

# speech data
Data, stop_words_array = init.readCSV()
Data_list = Data['speech'].values.tolist()
Data_length = len(Data_list)

processed_speeches = []

stop_words_array = []
with open(".\\app_files\stopwords.txt", "r", encoding="utf8") as file:
    for stopword in file.readlines():
        stopword = stopword[:-1]
        stop_words_array.append(stopword)

# processing each speech to remove punctuation and stopwords
for speech in Data_list:
    speech_list = speech.split(' ')
    # keeping only speeches with more than 100 words
    if (len(speech_list) > 100):
         text = dp.preprocess(speech, stop_words_array=stop_words_array)
         processed_speeches.append(text)

tfidf = TfidfVectorizer()
result = tfidf.fit_transform(processed_speeches)
lsa = TruncatedSVD(n_components = 20, n_iter = 100, random_state = 42) # n_compoments corresponds to number of topics
lsa.fit_transform(result)

"""
# Uncomment to print the topics with their terms
terms = tfidf.get_feature_names()

for index, component in enumerate(lsa.components_):
    zipped = zip(terms, component)
    top_terms_key = sorted(zipped, key = lambda t: t[1], reverse=True)[:5]
    top_terms_list = list(dict(top_terms_key).keys())
    print("Topic "+ str(index) + ": ", top_terms_list)"""

""" 
# topics and their most common words
Topic 0:  ['γιατι', 'κυριε', 'κυβερνηση', 'υπαρχει', 'εδω']
Topic 1:  ['ερωτηση', 'επικαιρη', 'αριθμο', 'βουλευτη', 'σχετικα']
Topic 2:  ['αρθρο', 'τροπολογια', 'αρθρου', 'βουλης', 'συζητηση']
Topic 3:  ['κυριοι', 'συναδελφοι', 'κυριες', 'βουλης', 'συνεδριαση']
Topic 4:  ['κατεθεσε', 'αναφορα', 'βουλευτης', 'ζητει', 'υγειας']
Topic 5:  ['βουλευτης', 'κατεθεσε', 'αναφορα', 'ζητει', 'κυριε']
Topic 6:  ['υγειας', 'μαθητες', 'θεωρεια', 'δυτικα', 'νοσοκομειο']
Topic 7:  ['υγειας', 'δημοκρατιας', 'συστημα', 'δημοκρατια', 'νοσοκομειο']
Topic 8:  ['υγειας', 'ευρω', 'αρθρο', 'τροπολογια', 'νοσοκομεια']
Topic 9:  ['υπουργειου', 'συζητηση', 'αρθρων', 'τροπολογιες', 'σχεδιου']
Topic 10:  ['τροπολογια', 'νομοσχεδιο', 'παιδειας', 'τροπολογιες', 'εκπαιδευση']
Topic 11:  ['ευρω', 'παιδειας', 'εργα', 'εργο', 'εκπαιδευσης']
Topic 12:  ['τροπολογια', 'ευρω', 'τροπολογιες', 'αφορα', 'θεμα']
Topic 13:  ['συζητηση', 'ευρω', 'ελλαδα', 'αρθρων', 'χιλιαδες']
Topic 14:  ['εργασιας', 'υπουργειου', 'εργαζομενων', 'εργαζομενους', 'εργαζομενοι']
Topic 15:  ['νομοσχεδιο', 'γιατι', 'εργα', 'κανουμε', 'αυτοδιοικηση']
Topic 16:  ['τροπολογια', 'υπουργε', 'χωρα', 'ελλαδα', 'αρθρο']
Topic 17:  ['τροπολογια', 'παιδειας', 'δημοκρατιας', 'πολιτικη', 'κυβερνηση']
Topic 18:  ['εργασιας', 'εργαζομενων', 'εργαζομενους', 'εργαζομενοι', 'εργα']
Topic 19:  ['τροπολογια', 'αγροτες', 'αυτοδιοικηση', 'χιλιαδες', 'αυτοδιοικησης']
Topic 20:  ['παρων', 'κυριοι', 'συναδελφοι', 'ψηφοφοριας', 'ιωαννης']
Topic 21:  ['ευρω', 'νομοσχεδιο', 'βουλης', 'διαδικασια', 'αγροτες']
Topic 22:  ['παρων', 'αυτοδιοικηση', 'αυτοδιοικησης', 'τοπικη', 'ευρω']
Topic 23:  ['δημοκρατιας', 'ευρω', 'παρων', 'αρθρο', 'νεας']
Topic 24:  ['νομοσχεδιο', 'υπουργος', 'κυβερνηση', 'κυριος', 'χιλιαδες']
Topic 25:  ['δεη', 'ενεργειας', 'επιχειρησεις', 'αυτοδιοικηση', 'αυτοδιοικησης']
Topic 26:  ['προβλημα', 'υπαρχει', 'νομου', 'σχεδιου', 'διαταξη']
Topic 27:  ['κυβερνηση', 'δεη', 'ενεργειας', 'υπουργος', 'κυριος']
Topic 28:  ['κυριοι', 'συναδελφοι', 'αρθρο', 'υπουργειο', 'αγροτες']
Topic 29:  ['τραπεζες', 'νομος', 'τραπεζα', 'νομου', 'κυβερνηση']
Topic 30:  ['δεη', 'συναδελφοι', 'κυριοι', 'ενεργειας', 'θεμα']
Topic 31:  ['επιτροπη', 'κυριοι', 'επιτροπης', 'προβλημα', 'υπουργε']
Topic 32:  ['δεη', 'συστημα', 'ενεργειας', 'ασφαλισης', 'συνταξη']
Topic 33:  ['κυβερνηση', 'νοσοκομειο', 'θεμα', 'πολιτικη', 'κανετε']
Topic 34:  ['αρθρο', 'δικαιοσυνης', 'υπουργος', 'αρθρα', 'κυριος']
Topic 35:  ['θεμα', 'νομος', 'προβλημα', 'ευρω', 'βουλης']
Topic 36:  ['δημοσιας', 'νομου', 'διοικησης', 'ευρω', 'αρθρου']
Topic 37:  ['νοσοκομειο', 'νομου', 'πω', 'θελω', 'δημοκρατιας']
Topic 38:  ['επιτροπη', 'προταση', 'πολιτικη', 'διαγραφεται', 'κωλυματος']
Topic 39:  ['πολιτικη', 'λεπτα', 'συστημα', 'υπουργος', 'εθνικης']
"""

# getting doc topic matrix
doc_topic = lsa.transform(result)
for n in range(doc_topic.shape[0]):
    topic_most_pr = doc_topic[n].argmax()
    f = open("doc_topics.txt", "a") 
    f.write("doc: {} topic: {}\n".format(n,topic_most_pr))
    f.close()