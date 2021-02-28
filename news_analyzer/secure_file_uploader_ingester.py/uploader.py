# Takes the file(s) that the user uploads and save it securely in the database
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
def uploader(file_URI, filetype):
    Response_headers : {# includes all infomration about this file
        "File" : {
            "User_ID" : (user_id, type=str) # generated
            "File_ID" : (file_id, type=str) # generated by uploader
            "Metadata" : (metadata, type=object) {
                "Created_At" : (created_at, type=str) # generated by uplodaer: yyyy-MM-dd HH:mm:ss
                "Updated_At" : (updated_at, type=str) # generated by uploader: yyyy-MM-dd HH:mm:ss
                "Size" : (size, type=str) # generated by uploader
                "Source" : (source, type=object) {
                        "Source" : (source, type=str) # if not given in request, means its from user o/w news_analyzer
                        "Search_param" : (search_param, type=list) # null if from user, search_param if from news_analyzer
                        "Filters" : (filters, type=list) # null if from user, filters if from news_analyzer
                }
            }
            "Permissions" : (permissions, type=object) {
                    "share_with" : [names] # default: user edit only
            }
            "Status" : (status, type=object) {
                "Uploader_status" : (uploader_status, type=str) # default: in_progress, uploader will update
            }
        }
    }
    return Response_headers

# possible logging
logging.info('file {filename} upload start', filename = file_name)
logging.info('file {filename} upload success', filename = file_name)
logging.error('file {filename} upload fail', filename = file_name)