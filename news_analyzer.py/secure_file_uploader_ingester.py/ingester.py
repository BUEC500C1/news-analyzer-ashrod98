# Takes file that the user uploads and the filetype, translates it to a raw .txt file
Request_headers: {
    "File" : {
        "File_Name": (file_name, type=str)
        "File_URI" : (file_uri, type=str)
        "File_Type" : (file_type, type=str) #.pdf, .doc, URL
        "Metadata" : (metadata, type=object) {
            "Author" : (author, type=str)
            "Published_At" : (published_at, type=str)
            "Source" : (source, type=object){
                "Source" : (source, type=str) # user or news_analyzer
                "Search_param" : (search_param, type=list) # null if from user, search_param if from news_analyzer
                "Filters" : (filters, type=list) # null if from user, filters if from news_analyzer
            }
        "Analyses" : (analyses, type=list) {
            [analysis wanted]
        }

        }
    }
}

    def ingester(file_URI, filetype):
        Response_headers: {
            "Text": (text, type=object){
                "Text" : (raw.txt, type=array)
            }
            "Status" : (status, type=object) {
                "Ingester_status": (ingester_status, type=str)
            }
        }
        return Response_headers
