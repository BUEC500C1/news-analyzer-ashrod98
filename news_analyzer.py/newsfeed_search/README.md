Newsfeed Ingester

Calls NY Time API to search based on keywords the user provides.
Will generate one output file per article requested.
These output files will be sent to the NLP module.

Procedural based API

Events:
    User_input_received
    Search_NYtimes_API 'searching APi'
    Receive_Response 'Articles found' 200
    Search_fail 401 = 'invaild API key', 429 = 'too many requests'

{
    "Newsfeed Ingester" : {}

        Arguments : [
                search_param : search parameters,
                numarticles : number of articles to return,
                filters : search filters
            ]
        Methods: {
            GET : /articlesearch.json

        }
        "Status" : [
            Searching_for_articles: {
                NYT API Repsonse: 200, 401, 429
            }
        ]
}
