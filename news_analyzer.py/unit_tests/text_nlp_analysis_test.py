# unit test for text nlp analysis module


# sunny day

# example.txt: My name is Ashley.
test_input : {
    "File_ID" : '12345678'
    "File_URI" : '~/Downloads'
    "Text" : 'example.txt'
    "Analyses" : {
        [
            'sentiment' = True,
            'names' = True,
            'common keywords' = True
        ]
    }
}

Response_headers : {
    "File_ID" : '12345678'
    "File_URI" : '~/Downloads'
    "Analyses" : { # not representative of actual NLP analysis
        "Sentiment" : 'neutral'
        "Keywords" : 'Ashley' 
        "Names" : 'Ashley'
    }
}

# bad day
