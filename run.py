from flask import Flask
from flask import request

app=Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return '<h1>The blog has started</>'

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

@app.route('/blog')
def blog():
    pass







if __name__ =='__main__':
    app.run(debug=True)


