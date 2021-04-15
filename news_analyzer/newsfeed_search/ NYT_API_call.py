# NY Times API call
# Base URI: https://api.nytimes.com/svc/search/v2/articlesearch.json
# Helpful links: https://developer.nytimes.com/docs/articlesearch-product/1/overview,
#                https://developer.nytimes.com/docs/semantic-api-product/1/overview
#                https://developer.nytimes.com/docs/articlesearch-product/1/routes/articlesearch.json/get
# returns json file with requested number of article URIs

import pyjq 
import requests
import math
from flask import Flask, redirect, request, url_for
API_KEY = 's0odA9LG8jtkAh3j6ll2WiOyHRQGtw0l'
secret = 'KyYBf1oAr3pFfxjG'
all_output = []

app = Flask(__name__)
@app.route('/')
def hello_world():
    return redirect('/NYT_API_CALL')

@app.route('/NYT_API_CALL', methods=['GET', 'POST'])
def api_call():
    if request.method == 'POST':
        if 'seach_param' not in request.form['search_param'] :
            flash('No input. Try again.')
            return redirect(request.url)
        search_param = request.form['search_param']
        if search_param == '':
            flash('No input, Try again.')
            return redirect(request.url)
        if num_articles == '':
            flash('No article amount specified.')
            return redirect(request.url)
        if num_articles <= 10:
            url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+search_param+'&api-key='+API_KEY
            r = requests.get(url)
            json_data = r.json()
            jq_query = f'.response .docs [] | {{web_url: .web_url}}'
            results = pyjq.all(jq_query, json_data)
            all_output.append = ([f'page 0', results])
        if num_articles >10:
            pages =  math.floor(num_articles/10)
            for page in range (pages):
                url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+search_param+'&page='+page+'&api-key='+API_KEY
                r = requests.get(url)
                json_data = r.json()
                jq_query = f'.response .docs [] | {{web_url: .web_url}}'
                results = pyjq.all(jq_query, json_data)
                all_output.append = ([f'page {page}', results])
        return redirect(url_for('show_results', all_output=all_output))
    return '''
    <!doctype html>
    <title>NYT API call</title>
    <h1>NYT API call</h1>
    <form method=post enctype=multipart/form-data>
    <input type=text name=search_param>
    <input type=number name=num_articles>
    <input type=submit value=Upload>
    </form>
    '''

@app.route('/API_call_results')
def show_results(all_output):
    return 'URL: '+all_output


# possible logging
# logging.error('API key invalid')
# logging.error('Too many searches')
