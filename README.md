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


Newsfeed Ingester

Calls NY Time API to search based on keywords the user provides.
Will generate one output file per article requested.
These output files will be sent to the NLP module.

Procedural based API


Text NLP Analysis

This module will received a .txt file and run an NLP analysis.
This includes searching for proper nouns, keywords, sentiment etc.
This module reqires user to define what to analyze for before doing so,
in order to reduce the time required to run, and reduce computational workload.
This module will output a file containing its analysis to the report generator.

Prodcedural based API
