# Main script that combines each function for this module

import user_request
import analysis

parameters = user_analyses_request()
files = user_file_request()

analyses = []
# run anlysis based on user requests

analysis_file = generate_analysis_file(*analyses)
