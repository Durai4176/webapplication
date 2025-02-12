from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask Webpage!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
