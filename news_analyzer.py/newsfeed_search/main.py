# Main script that combines each function for this module

import NYT_API_call
import Article_ingester

Request_headers : {
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
        "File_Name" : (file_name), type=str) # same as article title
        "File_URI" : (file_uri, type=str) # URL, from NYT API
        "File_Type" : (file_type, type=str) # 'URL'
        "Metadata" : (metadata, type=object) {
            "Author" : (author, type=str) # article.person(firstname, lastname) from NYT API
            "Published_At" : (published_at, type=str) # pub_date, from NYT API
            "Source" : (source, type=object){
                "Source" : (source, type=str) # user or news_analyzer (alt: article.source from NYT API)
                "Search_param" : (search_param, type=list) # null if from user, search_param if from news_analyzer
                "Filters" : (filters, type=list) # null if from user, filters if from news_analyzer
            }
        "Abstract" : (snippet, type=str) # from NYT API
        }
    "Article" : {}
    ]
    # generates

    return Response_headers
