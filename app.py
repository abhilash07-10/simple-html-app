from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def serve_form():
    return send_from_directory('.', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'age': request.form['age'],
        'message': request.form['message']
    }
    with open('submissions.txt', 'a') as f:
        f.write(str(data) + '\n')
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
