Secure File Uploader/Ingester:

Recives a file input from the user, and outputs a raw text file.
This output file will be sent to the Text NLP Analysis module.

Entitiy based API

Events:
    File_identify
    File_upload_fail 'file upload fail' 404
    File_upload_success 'file upload success' 200
    Generate_output_file 'file ingested' 200
    User_accept_output_file
    User_edit_output_file

{
    "Secure File Uploader" : [

    "File" : {
        "User_ID" : (user_id, type=str)
        "File_Name": (file_name, type=str)
        "File_URI" : (file_uri, type=str)
        "File_Type" : (file_type, type=str)
        "File_ID" : (file_id, type=str) # generated
        "Text_info": (text, type=object) {
            "Text" : (raw.txt, type=array)
            "Analyses" : (analyses, type=object) {
                "Sentiment" : (sentiment, type=str)
                "Keywords" : (keywords, type=list)
                [other analyses results]
            }
        }
        "Metadata" : (metadata, type=object) {
            "Author" : (author, type=str)
            "Created_At" : (created_at, type=str)
            "Updated_At" : (updated_at, type=str)
            "Published_At" : (published_at, type=str)
            "Size" : (size, type=str) # generated
            "Source" : (source, type=object) {
                    "Source" : (source, type=str)
                    "Search_param" : (search_param, type=list)
                    "Filters" : (filters, type=list)
            }
        }
        "Tags" : (tags, type=list) {
                [tags]
        }
        "Notes" : (notes, type=str)
        "Permissions" : (permissions, type=object) {
                "share_with" : [names]
        }
        "Status" : (status, type=object) {
            "Uploader_status" : (uploader_status, type=str)
            "Ingester_status": (ingester_status, type=str)
            "NLP_status" : (nlp_status, type=str)
        }
    }
    "File" : {...}
    ]
}
