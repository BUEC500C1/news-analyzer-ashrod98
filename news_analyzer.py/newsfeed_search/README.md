Newsfeed Ingester

Calls NY Time API to search based on keywords the user provides.
Will generate one output file per article requested.
These output files will be sent to the NLP module.

Procedural based API

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
