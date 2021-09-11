# Adding the project directory to python execution path

import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)

# Importing libraries
import logging
from src.utils.utils import Utilities
from src.exceptions.exceptions import CommandLineArgumentNotAvailable, InvalidFilePath
from src.message.message import Message


def main():
    
    try:
        #creating utility object
        utility = Utilities()
        
        # Fetching the properties
        properties = utility.read_config_properties(section_name = 'TAME OF THRONES')
        
        #fetching testfile path
        if len(sys.argv) < 2 :
            raise CommandLineArgumentNotAvailable
        else:
            input_file_abs_path = sys.argv[1]
            if not os.path.exists(input_file_abs_path):
                raise InvalidFilePath
        
        
        
        lines = utility.read_file_to_list_of_lines(input_file_abs_path)
        valid_kingdoms = []
        for line in lines:
            kingdom, message = line.split(" ")[0], " ".join(line.split(" ")[1:]).lower()
            message_obj = Message(kingdom, message)
            
            if message_obj.is_valid():
                valid_kingdoms.append(kingdom)
        
        # Check the allias it got
        if len(valid_kingdoms) >= 3:
            valid_kingdoms.insert(0, properties.get('message.sender.kingdom'))
        else:
            valid_kingdoms = []
        
        print(valid_kingdoms)
        return valid_kingdoms
    
    except CommandLineArgumentNotAvailable:
        logging.exception("Input file path is not provided.. \nplease run the code with input file path as first argument..")
    except InvalidFilePath:
        logging.exception("Path is invalid")
        
        
if __name__ == '__main__':
    main()