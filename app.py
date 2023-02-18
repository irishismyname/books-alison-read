from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! I'm Alison."
    return render_template('./static/index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=environ.get('PORT')
    )