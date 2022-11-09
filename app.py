from unittest import result
from flask import Flask, render_template, request, redirect, url_for
 
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
    data = [['sitting 1', 'speaker 1', 'lorem ipsum τεστ ελληνικά', 'fff'],
            ['sitting 2', 'speaker 2', 'lorem ipsum l', 'fffff'],
            ['sitting 3', 'speaker 1', 'lorem ipsum dolv d rfjgeg gerhngnerjkg  ergherjgn rgenerjnerg  regnerjkgnerk', 'fff'],
            ['sitting 4', 'speaker 3', 'lorem ipsum hsh', 'fff']]
    return render_template('result.html', queryDetails = data, uquery = results)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)