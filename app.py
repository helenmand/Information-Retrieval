from unittest import result
from flask import Flask, render_template, request, redirect, url_for
import query as q

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global results
    # reuest to search 
    if request.method == 'POST':
        results = request.form.get('query')  
        return redirect('/result')
        
    return render_template('index.html')

# Result page
@app.route('/result', methods=['GET', 'POST'])
def queries():
    global sitting_id, data, speaker_name, party_name
    data = q.get_random_data()
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
    
    return render_template('result.html', queryDetails = data, uquery = results)


@app.route('/sitting', methods=['GET', 'POST'])
def sitting():
    global sitting_id, data, speaker_name, party_name
    dt = data[int(sitting_id)][1:]

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

    return render_template('sitting.html', toPrint = dt)

@app.route('/speaker', methods=['GET', 'POST'])
def speaker():
    global sitting_id, data, speaker_name, party_name
    dt = q.sittings_by_speaker(speaker_name)
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

    return render_template('speaker.html', sittings = dt, speaker_name = speaker_name), 404

@app.route('/party', methods=['GET', 'POST'])
def party():
    global sitting_id, data, speaker_name, party_name
    dt = q.sittings_by_party(party_name)
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

    return render_template('party.html', sittings = dt, party_name = party_name), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)