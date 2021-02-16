# Main script that combines each function for this module

user_input = [input_file, file_type]
state = uploader(input_file, file_type)
if state is True:
    raw_text_file = ingester(input_file, file_type)
