EC500A2 HOMEWORK 2 PHASE 1

API MODULES

news_analyzer: {
    Secure File Uploader/Ingester,
    Text NLP Analysis,
    News feeed Ingester
}


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
    
        "Data" : {
            "Original_file": "file.txt"
            "Ingester_output": "raw.txt"
            "Error": bool
            "User_accept": bool
        }
        {
            ""Repeat with other file inputs""
        }
    ]
}


Newsfeed Ingester

Calls NY Time API to search based on keywords the user provides.
Will generate one output file per article requested.
These output files will be sent to the NLP module.

Procedural based API

*Should article URIs will be saved in another file for record keeping

Events:
    User_input_received (status)
    Search_NYtimes_API (process)
    Receive_URI (status)
    Translate_article_to_text (process)
    Generate_output_files (status)

{
    "Newsfeed Ingester" : [

        "Arguments" : {
            "User_input_attributes": [
                keywords,
                number of articles,
                filters
            ]
        }
        "Methods":{
            "user_input" : user_input(*parameters)
            "NY_times_API_call" : NY_times_API_call()
            "translate_article_to_text" : translate_article_to_text(URI)
            "generate_output_text_file" : generate_output_text_file(*file)
        }
        "Status" : [
            User_input_received
            Searching_for_articles
            Translating_articles
            Generating_output_files
        ]
    ]
}


Text NLP Analysis

This module will received a .txt file and run an NLP analysis.
This includes searching for proper nouns, keywords, sentiment etc.
This module reqires user to define what to analyze for before doing so,
in order to reduce the time required to run, and reduce computational workload.
This module will output a file containing its analysis to the report generator.

Prodcedural based API

Events:
    Input_file_received (status)
    Analysis_parameters_received (status)
    Start_analysis (process)
    Analysis_failed (status)
    Analysis_succeeded (status)
    Analysis_in_progress (status)
    Generate_output_file (status)

{
    "Input Data" : [
        analysis parameters,
        file
    ]
    "Methods" : [
        "user_analyses_request" : user_analyses_request()
        "file search": file_search(parameter, *files)
        "find_common_keywords": find_common_keyword(*keywords, *files)
        "find_names": find_names(*files)
        "find_locations": find_locations(&files)
        "find_address": find_address(*files)
        "keyword relations": find_relations(*files)
        "find_sentiment" : find_sentiment(*files)
        "modify_sentiment": modify_sentiment(sentiment, *file)
        "keyword search": keyword_serach(*keywords, *files)
        "summary": summary(*files)
        "snapshot": snapshot(*files)
        "generate_analysis_file" : generate_analysis_file(*file)
    ]
    "Status" : [
        User_input_reciever
        File_input_found
        Analyzing
        Generating_analysis_file
    ]
}