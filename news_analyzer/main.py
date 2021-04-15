from flask import Flask, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)
URL = ("mongodb+srv://ashrod98:0042855@newsanalyzerdata.b"
         "igfx.mongodb.net/myFirstDatabase?retryWrites=true"
         "&w=majority")

mongo = PyMongo.MongoClient(URL)
mydb = mongo['mydatabase']


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/newsfeed_search', methods=['GET'])
def newsfeed_search():
    return render_template('newsfeed_search.html')


@app.route('/secure_file_uploader_ingester', methods=['GET', 'POST'])
def secure_file_uploader_ingester():
    return render_template('secure_file_uploader_ingester.html')


@app.route('/text_nlp_analysis', methods=['GET'])
def text_nlp_analysis():
    return render_template('text_nlp_analysis')


if __name__ == "__main__":
    app.run(debug=True)