from unittest import result
from flask import Flask, render_template, request, redirect, url_for
import query as q
 
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global results
    if request.method == 'POST':
        results = request.form.get('query')  
        return redirect('/result')
        
    return render_template('index.html')

# Result page
@app.route('/result', methods=['GET', 'POST'])
def queries():
    global link1
    if request.method == 'POST':
        link1 = request.form.get('query')   
        return redirect('/sitting')
    """data = [
            ['sitting 1', 'speaker 1', 'ffff', 'Lorem ipsum dolor sit amet. Aut error commodi ut ipsum voluptatem aut facere', '1'],
            ['sitting 2', 'speaker 2', 'ffff', 'Lorem ipsum dolor sit amet. Aut error commodi ut ipsum voluptatem aut facere', '0.5'],
            ['sitting 3', 'speaker 1', 'ffff', 'Lorem ipsum dolor sit amet. Aut error commodi ut ipsum voluptatem aut facere', '0.2'],
            ['sitting 4', 'speaker 3', 'ffff', 'Lorem ipsum dolor sit amet. Aut error commodi ut ipsum voluptatem aut facere', '0.9'],
            ['sitting 5', 'speaker 2', 'ffff', 'Lorem ipsum dolor sit amet. Aut error commodi ut ipsum voluptatem aut facere', '0.4'],
            ]"""
    global data 
    data = q.get_random_data()
    return render_template('result.html', queryDetails = data, uquery = results)

@app.route('/sitting', methods=['GET', 'POST'])
def sitting():
    dt = data[int(link1)][1:]
    return render_template('sitting.html', toPrint=dt)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)