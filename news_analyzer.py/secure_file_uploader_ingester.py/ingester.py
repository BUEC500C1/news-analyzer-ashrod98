# Takes file that the user uploads and the filetype, translates it to a raw .txt file

    def ingester(file_URI, filetype):
        Response_headers :
        "Text": (text, type=object){
            "Text" : (raw.txt, type=array)
        }
        "Metadata" : (metadata, type=object) {
            "Size" : (size, type=str)
        }
        "Status" : (status, type=object) {
            "Ingester_status": (ingester_status, type=str)
        }
        return Response_headers
