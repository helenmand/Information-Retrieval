import csv
import random
import string

def get_random_data():
    sittings = []
    # 0:'member_name', 1:'sitting_date', 'parliamentary_period', 'parliamentary_session', 4:'parliamentary_sitting', 
    # 'political_party', 'government', 'member_region', 'roles', 'member_gender', 'speech
    with open('Greek_Parliament_Proceedings_1989_2020_DataSample.csv','r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            speech_sample = [random.choice(row[10].split(' ')) for _ in range(0,5)]
            speech_sample = (' '.join(speech_sample)).translate(str.maketrans('', '', string.punctuation))
            sittings.append([row[4], row[0], row[1], speech_sample, random.randint(0,100)/100])
            
    return random.sample(sittings, 5)