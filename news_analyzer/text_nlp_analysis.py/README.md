Text NLP Analysis

This module will received a .txt file and run an NLP analysis.
This includes searching for proper nouns, keywords, sentiment etc.
This module reqires user to define what to analyze for before doing so,
in order to reduce the time required to run, and reduce computational workload.
This module will output a file containing its analysis to the report generator.

Prodcedural based API

Events:
    Input_file_received = raw text file found
    Analysis_parameters_received = valid input
    Start_analysis
    Analysis_in_progress
    Analysis_fail
    Analysis_success 
    Generate_output_file

{
    Input Data : [
        analysis parameters,
        file
    ]
    Methods : [
        find_names: find_names(file)
        find_locations: find_locations(file)
        find_addresses: find_address(file)
        keyword relations: find_relations(file)
        find_sentiment : find_sentiment(file)
        modify_sentiment: modify_sentiment(sentiment, file)
        keyword_search: keyword_serach(keywords, file)
        summary: summary(file)
        snapshot: snapshot(file)
        generate_analysis_file : generate_analysis_file(file)
    ]
    Status : [
        User_input_recieved
        File_input_found
        Analyzing
        Generating_analysis_file
        Analysis_complete
    ]
}
