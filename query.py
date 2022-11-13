import csv
import random
import string

def clean_tags(text):
    speech_sample = [random.choice(text.split(' ')) for _ in range(0,5)]
    speech_sample = (' '.join(speech_sample)).translate(str.maketrans('', '', string.punctuation))
    return speech_sample

def get_random_data():
    sittings = []
    # 0:'member_name', 1:'sitting_date', 'parliamentary_period', 'parliamentary_session', 4:'parliamentary_sitting', 
    # 5: 'political_party', 'government', 'member_region', 'roles', 'member_gender', 'speech
    with open('Greek_Parliament_Proceedings_1989_2020_DataSample.csv','r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            speech_sample = clean_tags(row[10])
            sittings.append([row[4], row[0], row[5], speech_sample, random.randint(0,100)/100])
    
    sample = random.sample(sittings, 5)
    for i in range(0,5):
        sample[i].insert(0, i)

    return sample

def sittings_by_speaker(speaker):
    sittings = []
    with open('Greek_Parliament_Proceedings_1989_2020_DataSample.csv','r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0].lower() == speaker:
                speech_sample = clean_tags(row[10])
                sittings.append([row[4], row[5], speech_sample])
        return sittings

def sittings_by_party(party):
    sittings = []
    with open('Greek_Parliament_Proceedings_1989_2020_DataSample.csv','r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[5].lower() == party:
                speech_sample = clean_tags(row[10])
                sittings.append([row[4], row[0], speech_sample])
        return sittings
