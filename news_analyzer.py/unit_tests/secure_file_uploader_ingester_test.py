# unit test for secure file uploader ingester module

# sunny day
test_input : {
    "File" : {
        "File_Name": 'example.pdf'
        "File_URI" : '~/Downloads'
        "File_Type" : 'pdf'
        "Metadata" : {
            "Author" : 'Ashley Rodriguez'
            "Source" : {
                "Source" : 'user' # user or news_analyzer
            }
        "Analyses" : (analyses, type=list) {
            ['sentiment', 'common keywords', 'names']
        }
}

expected_output : {
    "File" : {
        "User_ID" : 'U11249887' # my bu id, but could be something else
        "File_Name": 'example.pdf'
        "File_URI" : '~/Downloads''
        "File_Type" : 'pdf''
        "File_ID" : '12345678' # would be random 8 digit number
        "Text_info": {
            "Text" : 'This is an example file.' # example.pdf held this text
            "Analyses" : {
                "Sentiment" : neutral
                "Keywords" : null
                "Names" : null 
            }
        }
        "Metadata" : {
            "Author" : 'Ashley Rodriguez'
            "Created_At" : '2021-02-20 19:57:34'
            "Updated_At" : '2021-02-20 20:00:00'  #added time for NLP analysis, not representative of actual module
            "Published_At" : null
            "Size" : '150 kilobytes' # not representative of actual file size
            "Source" : (source, type=object) {
                    "Source" : user
                    "Search_param" : null
                    "Filters" : null
            }
        }
        "Tags" : 
                null
        }
        "Notes" : null
        "Permissions" : 
                "share_with" : null
        }
        "Status" : (status, type=object) {
            "Uploader_status" : 'File upload success'
            "Ingester_status": 'File ingested'
            "NLP_status" : 'Analysis complete'
        }
    }
}

