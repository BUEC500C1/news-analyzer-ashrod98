# main script that combines each function for this module
import NYT_API_call
import Article_ingester
import user_request

parameters = parameter_request() 
num_articles = num_articles_request()
URIs = NYT_API_call(parameters, num_articles)

output_text_files = []

for x in URIs 
    output_text_file = Article_ingester(x)
