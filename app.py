from unittest import result
from flask import Flask, render_template, request, redirect
import query as q
import data_processing as dp
import initialize as init

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global uquery, fs, squery
    
    # reuest to search 
    if request.method == 'POST':
        squery = request.form.get('query')
        uquery, query_tags = dp.process(str(squery), stop_words_array)
        fs = 1

        # bad query
        if (type(uquery) is int):
            return redirect('404.html')

        return redirect('/result')
        
    return render_template('index.html')

# Result page
@app.route('/result', methods=['GET', 'POST'])
def queries():
    global sitting_id, data, speaker_name, party_name, squery, uquery, querries, fs

    if fs == 1:
        data = q.get_sittings(uquery, Data, Docs, tags_dict)
        querries = render_template('result.html', queryDetails = data, uquery = squery)

    # request to view more info about the sitting , the speaker or the political party
    if request.method == 'POST':
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')   
            return redirect('/sitting')
        elif "speaker" in request.form:
            speaker_name = request.form.get('speaker')
            return redirect('/speaker')
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')
            
    return querries


@app.route('/sitting', methods=['GET', 'POST'])
def sitting():
    global sitting_id, data, speaker_name, party_name, Data, tags_dict, fs
    data = q.get_sitting_info(sitting_id, Data, tags_dict)
    fs += 1

    # request to view more info about the speaker or the political party
    if request.method == 'POST':
        if "speaker" in request.form:
            speaker_name = request.form.get('speaker')
            return redirect('/speaker')
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')

    return render_template('sitting.html', toPrint = data)

@app.route('/speaker', methods=['GET', 'POST'])
def speaker():
    global sitting_id, data, speaker_name, party_name, Data, tags_dict, member_dict, fs
    sittings = q.get_sittings_by_speaker(speaker_name, Data, tags_dict, member_dict)
    fs += 1

    # request to view more info about the sitting or the political party
    if request.method == 'POST':
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')   
            return redirect('/sitting')
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')

    return render_template('speaker.html', sittings = sittings, speaker_name = speaker_name), 404

@app.route('/party', methods=['GET', 'POST'])
def party():
    global sitting_id, data, speaker_name, party_name, Data, tags_dict, party_dict, member_dict, fs
    data = q.get_sittings_by_party(party_name, Data, tags_dict, party_dict, member_dict)
    fs += 1

    # request to view more info about the sitting or the speaker
    if request.method == 'POST':
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')   
            return redirect('/sitting')
        elif "speaker" in request.form:
            speaker_name = request.form.get('speaker')
            return redirect('/speaker')

    return render_template('party.html', sittings = data, party_name = party_name), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    global Data, Docs, member_dict, party_dict, tags_dict, stop_words_array, fs
    Data, Docs, stop_words_array, member_dict, party_dict, tags_dict = init.init()
    fs = 0
    app.run(debug=True)