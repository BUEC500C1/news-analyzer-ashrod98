# Main script that combines each function for this module

import NYT_API_call
import Article_ingester
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
Request_headers: {
    "search_param" : (search_param, type=list) {
        [keywords]
    }
    "number of articles" : (num_articles, type=int)
    "filters" : (filters, type=list) [
        #TBA, look at NYTimes filters
    ]
}

def newsfeed_search(Request_headers)
    # search NYT API with given arguments
    Response_headers : [
    "Article" : {
        "File_Name" : (file_name), type=str) # same as article title, user may edit later
        "File_URI" : (file_uri, type=str) # URL, from NYT API
        "File_Type" : (file_type, type=str) # 'URL'
        "Metadata" : (metadata, type=object) {
            "Author" : (author, type=str) # article.person(firstname, lastname) from NYT API
            "Published_At" : (published_at, type=str) # pub_date, from NYT API
            "Source" : (source, type=object) {
                "Source" : (source, type=str) # news_analyzer (alt: article.source from NYT API)
                "Search_param" : (search_param, type=list) # search_param used to find it
                "Filters" : (filters, type=list) # filters used to fild it
            }
        }
    "Article" : {...}
    ]
    # generates

    return Response_headers

# possible logging
logging.info('Searching for articles')
logging.info('Search complete')
logging.error('No articles found')
