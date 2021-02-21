Newsfeed Ingester

Calls NY Time API to search based on keywords the user provides.
Will generate one output file per article requested.
These output files will be sent to the NLP module.

Procedural based API

Events:
    User_input_received
    Search_NYtimes_API
    Receive_Response

{
    "Newsfeed Ingester" : {}

        Arguments : [
                search_param : search parameters,
                numarticles : number of articles to return,
                filters : serach filters
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
