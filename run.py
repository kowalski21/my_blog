from flask import Flask

app=Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return '<h1>The blog has started</>'






if __name__ =='__main__':
    app.run(debug=True)


