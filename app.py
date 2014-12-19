from flask import Flask, render_template, redirect
from settings import DEBUG, URLS


app = Flask(__name__)
app.debug = DEBUG


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


#@app.route('/blog', methods=['GET'])
#def blog():
#    return redirect(URLS['blog'])


#@app.route('/twitter', methods=['GET'])
#def twitter():
#    return redirect(URLS['twitter'])


#@app.route('/youtube', methods=['GET'])
#def youtube():
#    return redirect(URLS['youtube'])


#@app.route('/store', methods=['GET'])
#def store():
#    return redirect(URLS['store'])


if __name__ == '__main__':
    app.run()