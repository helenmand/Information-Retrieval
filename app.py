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
    data = results
    return render_template('result.html', uquery = data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)