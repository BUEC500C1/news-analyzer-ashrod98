from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/newsfeed_search')
def newsfeed_search():
    return 'news feed search'


@app.route('/secure_file_uploader_ingester')
def secure_file_uploader_ingester():
    return 'secure_file_uploader_ingester'


@app.route('/text_nlp_analysis')
def text_nlp_analysis():
    return 'text_nlp_analysis'


if __name__ == "__main__":
    app.run(debug=True)