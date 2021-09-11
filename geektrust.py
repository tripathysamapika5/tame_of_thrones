# Adding the project directory to python execution path

import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)

# Importing libraries
import logging
from src.utils.utils import Utilities
from src.exceptions.exceptions import CommandLineArgumentNotAvailable, InvalidFilePath
from src.utils.message_validation_util import Message_Validation_Util

def main():
    
    try:
        #creating utility object
        utility = Utilities()
        message_validation_utility_obj = Message_Validation_Util(utility)
               
        #fetching testfile path
        input_file_abs_path = utility.fetch_input_file_path_from_cli(sys.argv)
        
        #Getting the valid kingdoms where support was received
        valid_kingdoms = message_validation_utility_obj.find_valid_kingdoms_from_input_file(input_file_abs_path)
        
        print(valid_kingdoms)
    
    except CommandLineArgumentNotAvailable:
        logging.exception("Input file path is not provided.. \nplease run the code with input file path as first argument..")
    except InvalidFilePath:
        logging.exception("Path is invalid")
        
        
if __name__ == '__main__':
    main()