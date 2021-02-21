# Output file generator

Request_headers : {
    "Text" : (raw.txt, type=array)
    "Analyses" : (analyses, type=list) {
        [analysis wanted, type=bool]
    }

# generate analysis file
def generate_analysis_file(analyses):
    # parses analyses list of bools to see what analyses to call from analysis.py

    Response_headers: {
    "Analyses" : (analyses, type=object) { # generated
            "Sentiment" : (sentiment, type=str)
            "Keywords" : (keywords, type=list)
            [other analyses results]
        }
    }
    return Response_headers
