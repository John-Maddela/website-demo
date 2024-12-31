
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory data storage for demo
stories = []

@app.route('/')
def index():
    return render_template('index.html', stories=stories)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        stories.append({'title': title, 'content': content})
        return redirect('/')
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
