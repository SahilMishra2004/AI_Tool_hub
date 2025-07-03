from flask import Flask, render_template, request
from summarize import summarize_text
from humanize import humanize_text
from detect_ai import detect_ai_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        result = summarize_text(text)
    return render_template('summarize.html', result=result)

@app.route('/humanize', methods=['GET', 'POST'])
def humanize():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        result = humanize_text(text)    
    return render_template('humanize.html', result=result)

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        result = detect_ai_text(text)
    return render_template('detect.html', result=result)
@app.route("/3")
def fun():
    return render_template("3.html")
if __name__ == '__main__':
    app.run(debug=True)
