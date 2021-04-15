# Takes file that the user uploads and the filetype, translates it to a raw .txt file

# Request_headers: {
#     "File" : {
#         "File_Name": (file_name, type=str)
#         "File_URI" : (file_uri, type=str)
#         "File_Type" : (file_type, type=str) #.pdf, .doc, URL
#         "Metadata" : (metadata, type=object) {
#             "Author" : (author, type=str)
#             "Published_At" : (published_at, type=str)
#             "Source" : (source, type=object){
#                 "Source" : (source, type=str) # user or news_analyzer
#                 "Search_param" : (search_param, type=list) # null if from user, search_param if from news_analyzer
#                 "Filters" : (filters, type=list) # null if from user, filters if from news_analyzer
#             }
#         "Analyses" : (analyses, type=list) {
#             [analysis wanted]
#         }

#         }
#     }
# }

# Response_headers: {
#     "Text": (text, type=object){
#         "Text" : (raw.txt, type=array)
#     }
#     "Status" : (status, type=object) {
#         "Ingester_status": (ingester_status, type=str)
#     }
# }
# possible logging
# logging.info('Ingesting start')
# logging.error('Ingesting fail')
# logging.info('Ingesting complete')



from pdfminer.high_level import extract_text

def pdf_to_txt(file_path):

    text = extract_text(file_path)
    with open("PDFIngested.txt", 'w') as ingested:
        print(text, file=ingested)

    ingested.close()
