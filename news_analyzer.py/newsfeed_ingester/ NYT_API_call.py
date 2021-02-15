# NY Times API call
# Base URI: https://api.nytimes.com/svc/search/v2/articlesearch.json
# Helpful links: https://developer.nytimes.com/docs/articlesearch-product/1/overview, 
#                https://developer.nytimes.com/docs/semantic-api-product/1/overview
#                https://developer.nytimes.com/docs/articlesearch-product/1/routes/articlesearch.json/get
# returns json file with requested number or article URIs

def NYT_API_call(*parameters, num_articles):
    return URI_list