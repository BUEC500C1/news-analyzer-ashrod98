Secure File Uploader/Ingester:

Recives a file input from the user, and outputs a raw text file.
This output file will be sent to the Text NLP Analysis module.

Entitiy based API

Events:
    File_identify (status)
    File_upload_start (process)
    error_check (process)
    File_upload_fail (status)
    File_upload_succeed (status) 
    User_accept_output_file (status)
    User_edit_output_file (process)
    Generate_output_file (status)

{
    "Secure File Uploader" : [
    
        "File" : {
            "User_ID" : (user_id, type=str) 
            "File_Name": (file_name, type=str) 
            "File_URI" : (file_uri, type=str) 
            "File_Type" : (file_type, type=str) 
            "File_ID" : (file_id, type=str) 
            "Text": (text, type=object) {
                "Text" : (raw.txt, type=array) 
                "Sentiment" : (sentiment, type=str) 
                "Keywords" : (keywords, type=list) 
                [other analyses paramters]
            }
            "Metadata" : (metadata, type=object) {
                "Author" : (author, type=str) 
                "Created_At" : (created_at, type=str) 
                "Updated_At" : (updated_at, type=str) 
                "Published_At" : (published_at, type=str) 
                "Size" : (size, type=str) 
                "Source" : (source, type=object) {
                    "Source" : (source, type=str) 
                    "Search_param" : (search_param, type=list) 
                    "Filters" : (filters, type=list) 
                }
            }
            "Tags" : (tags, type=list) { # null, user generated
                [tags]
            }
            "Notes" : (notes, type=str) # null, user generated
            "Permissions" : (permissions, type=object) {
                "share_with" : [names] # user generated, default: user edit only
            }
            "Status" : (status, type=object) {
                "Uploader_status" : (uploader_status, type=str) # default: in_progress, uploader will update
                "Ingester_status": (ingester_status, type=str) # default: stand_by, ingester will update
                "NLP_status" : (nlp_status, type=str) # default: stand_by, text_nlp_analysis will update
        }
    )
    
    ]
}