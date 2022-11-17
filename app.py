from unittest import result
from flask import Flask, render_template, request, redirect, url_for
import query as q
import data_processing as dp
import initialize as init

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global uquery
    # reuest to search 
    if request.method == 'POST':
        uquery, query_tags = dp.process(str(request.form.get('query')), stop_words_array)
            
        if (type(uquery) is int):
            return redirect('404.html')

        return redirect('/result')
        
    return render_template('index.html')

# Result page
@app.route('/result', methods=['GET', 'POST'])
def queries():
    global sitting_id, data, speaker_name, party_name, uquery
    data = q.get_sittings(uquery, Data, Docs, tags_dict)
    # request to view more info about
    if request.method == 'POST':
        # the sitting
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')   
            return redirect('/sitting')
        # the speaker
        elif "speaker" in request.form:
            speaker_name = request.form.get('speaker')
            return redirect('/speaker')
        # or the political party
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')
    
    return render_template('result.html', queryDetails = data, uquery = uquery)


@app.route('/sitting', methods=['GET', 'POST'])
def sitting():
    global sitting_id, data, speaker_name, party_name, Data, tags_dict
    data = q.get_sitting_info(sitting_id, Data, tags_dict)

    # request to view more info about
    if request.method == 'POST':
        # the speaker
        if "speaker" in request.form:
            speaker_name = request.form.get('speaker')
            return redirect('/speaker')
        # or the political party
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')

    return render_template('sitting.html', toPrint = data)

@app.route('/speaker', methods=['GET', 'POST'])
def speaker():
    global sitting_id, data, speaker_name, party_name, Data, tags_dict, member_dict
    sittings = q.get_sittings_by_speaker(speaker_name, Data, tags_dict, member_dict)
    # request to view more info about
    if request.method == 'POST':
        # the sitting
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')   
            return redirect('/sitting')
        # or the political party
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')

    return render_template('speaker.html', sittings = sittings, speaker_name = speaker_name), 404

@app.route('/party', methods=['GET', 'POST'])
def party():
    global sitting_id, data, speaker_name, party_name, Data, tags_dict, party_dict, member_dict
    data = q.get_sittings_by_party(party_name, Data, tags_dict, party_dict, member_dict)
    # request to view more info about
    if request.method == 'POST':
        # the sitting
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')   
            return redirect('/sitting')
        # or the speaker
        elif "speaker" in request.form:
            party_name = request.form.get('speaker')
            return redirect('/speaker')

    return render_template('party.html', sittings = data, party_name = party_name), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    global Data, Docs, member_dict, party_dict, tags_dict, stop_words_array 
    Data, Docs, stop_words_array, member_dict, party_dict, tags_dict = init.init()
    app.run(debug=False)