import data_processing as dp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import data_processing as dp
import initialize as init

# speech data
Data, stop_words_array = init.readCSV()
Data_list = Data['speech'].values.tolist()
Data_length = len(Data_list)

processed_speeches = []

stop_words_array = []
with open("stopwords.txt", "r", encoding="utf8") as file:
	for stopword in file.readlines():
		stopword = stopword[:-1]
		stop_words_array.append(stopword)

# processing each speech to remove punctuation and stopwords
for speech in Data_list:
	speech_list = speech.split(' ')
    # keeping only speeches with more than 100 words
	if (len(speech_list) > 100):	
		#text = dp.punctuation_removal(speech)
		text = dp.stop_word_removal(speech, stop_words_array=stop_words_array)

		processed_speeches.append(text)

tfidf = TfidfVectorizer()
result = tfidf.fit_transform(processed_speeches)
lsa = TruncatedSVD(n_components = 40, n_iter = 100, random_state = 42)
lsa.fit_transform(result)

# Get Singular values and Components 
Sigma = lsa.singular_values_ 
V_transpose = lsa.components_.T

# Print the topics with their terms
terms = tfidf.get_feature_names()

for index, component in enumerate(lsa.components_):
    zipped = zip(terms, component)
    top_terms_key=sorted(zipped, key = lambda t: t[1], reverse=True)[:5]
    top_terms_list=list(dict(top_terms_key).keys())
    print("Topic "+str(index)+": ",top_terms_list)

"""
Topic 0:  ['γιατι', 'κυριε', 'κυβερνηση', 'υπαρχει', 'εδω']
Topic 1:  ['ερωτηση', 'επικαιρη', 'αριθμο', 'βουλευτη', 'σχετικα']
Topic 2:  ['αρθρο', 'τροπολογια', 'αρθρου', 'βουλης', 'συζητηση']
Topic 3:  ['κυριοι', 'συναδελφοι', 'κυριες', 'βουλης', 'συνεδριαση']
Topic 4:  ['κατεθεσε', 'αναφορα', 'βουλευτης', 'ζητει', 'υγειας']
Topic 5:  ['βουλευτης', 'κατεθεσε', 'αναφορα', 'ζητει', 'κυριε']
Topic 6:  ['υγειας', 'μαθητες', 'θεωρεια', 'δυτικα', 'μαθητριες']
Topic 7:  ['υγειας', 'δημοκρατιας', 'συστημα', 'δημοκρατια', 'νοσοκομειο']
Topic 8:  ['υγειας', 'ευρω', 'αρθρο', 'τροπολογια', 'δισεκατομμυρια']
Topic 9:  ['υπουργειου', 'συζητηση', 'αρθρων', 'τροπολογιες', 'σχεδιου']
Topic 10:  ['τροπολογια', 'νομοσχεδιο', 'παιδειας', 'τροπολογιες', 'εκπαιδευση']
Topic 11:  ['ευρω', 'παιδειας', 'σο', 'πα', 'εργα']
Topic 12:  ['υπουργε', 'κυριε', 'πα', 'σο', 'αγροτες']
Topic 13:  ['τροπολογια', 'κυβερνηση', 'πα', 'σο', 'δημοσιου']
Topic 14:  ['πα', 'σο', 'αγροτες', 'αρθρο', 'αγροτων']
Topic 15:  ['εργασιας', 'εργαζομενων', 'υπουργειου', 'θεμα', 'υπουργειο']
Topic 16:  ['κυριε', 'υπουργε', 'τροπολογια', 'προεδρε', 'αρθρο']
Topic 17:  ['συναδελφοι', 'κυριε', 'υπουργε', 'δικαιοσυνης', 'κυριοι']
Topic 18:  ['εργασιας', 'σο', 'πα', 'χιλιαδες', 'εργαζομενων']
Topic 19:  ['πα', 'σο', 'τροπολογια', 'ευρω', 'δικαιοσυνης']
Topic 20:  ['πα', 'σο', 'ευρω', 'κυριε', 'υπουργε']
Topic 21:  ['παρων', 'κυριοι', 'συναδελφοι', 'κυριες', 'ψηφοφοριας']
Topic 22:  ['συναδελφοι', 'αρθρο', 'κυριοι', 'προβλημα', 'εργασιας']
Topic 23:  ['παρων', 'αυτοδιοικηση', 'ευρω', 'αυτοδιοικησης', 'τοπικη']
Topic 24:  ['δημοκρατιας', 'ευρω', 'νομοσχεδιο', 'παρων', 'αρθρο']
Topic 25:  ['νομοσχεδιο', 'υπουργος', 'κυριος', 'χιλιαδες', 'κυβερνηση']
Topic 26:  ['δεη', 'ενεργειας', 'επιχειρησεις', 'αυτοδιοικηση', 'αυτοδιοικησης']
Topic 27:  ['προβλημα', 'υπαρχει', 'νομου', 'σχεδιου', 'διαταξη']
Topic 28:  ['δεη', 'κυβερνηση', 'ενεργειας', 'υπουργος', 'κυριος']
Topic 29:  ['κυριοι', 'συναδελφοι', 'κυριες', 'αρθρο', 'υπουργειο']
Topic 30:  ['τραπεζες', 'ευρωπαϊκη', 'νομος', 'τραπεζα', 'ρυθμιση']
Topic 31:  ['δεη', 'ενεργειας', 'συναδελφοι', 'κυριοι', 'θεμα']
Topic 32:  ['επιτροπη', 'βουλης', 'υπουργε', 'δημοκρατιας', 'επιτροπης']
Topic 33:  ['συστημα', 'δεη', 'ενεργειας', 'ασφαλισης', 'συνταξη']
Topic 34:  ['κυβερνηση', 'νοσοκομειο', 'θεμα', 'αρθρο', 'κανετε']
Topic 35:  ['αρθρο', 'δικαιοσυνης', 'υπουργος', 'αρθρα', 'κυριος']
Topic 36:  ['θεμα', 'νομος', 'προβλημα', 'βουλης', 'ευρω']
Topic 37:  ['δημοσιας', 'νομου', 'διοικησης', 'ευρω', 'αρθρου']
Topic 38:  ['νοσοκομειο', 'νομου', 'πω', 'θελω', 'σχεδιο']
Topic 39:  ['επιτροπη', 'αρθρου', 'προταση', 'κωλυματος', 'διαγραφεται']
Topic 40:  ['πολιτικη', 'λεπτα', 'συστημα', 'υπουργος', 'ευρω']
"""