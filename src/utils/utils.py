import configparser
import os 
import string
from src.exceptions.exceptions import CommandLineArgumentNotAvailable, InvalidFilePath


class Utilities:
                   
    def interpret(self, val):
        try:
            return eval(val)
        except:
            return val
        
    def find_absolute_path(self, relative_file_path):
        working_dir = os.getcwd()
        abs_config_file_path = os.path.join(working_dir, relative_file_path)
        return abs_config_file_path
    
    def find_config_file_path(self, env = 'prod'):
        relative_file_path = 'src/resources/app-config.properties'
        
        if env == 'test':
            relative_file_path = '-test.'.join(relative_file_path.split('.'))
            
        abs_config_file_path = self.find_absolute_path(relative_file_path)
        
        return abs_config_file_path
            
    def read_config_properties(self, section_name, env = 'prod'):
        
        abs_config_file_path = self.find_config_file_path(env)
        
        config = configparser.RawConfigParser()
        config.read(abs_config_file_path)
        properties = dict(config.items(section_name))
        for key in properties:
            properties[key] = self.interpret(properties[key])
        
        return   properties 
    
    def get_kingdom_to_emblame_mapping(self):
        properties = self.read_config_properties(section_name = 'TAME OF THRONES')
        return properties.get('kingdom.to.emblame.mapping')

    def get_message_sender_name(self):
        properties = self.read_config_properties(section_name = 'TAME OF THRONES')
        return properties.get('message.sender.kingdom')

    
    def read_file_to_list_of_lines(self, file_path):
        with open(file_path) as f:
            lines = f.readlines()
        return lines
    
    def get_all_alphabets(self):
        return string.ascii_lowercase
    
    def iterable_item_counter(self, iterable):
        result = {elem : 0 for elem in sorted(iterable)}
        for elem in iterable:
            result[elem] += 1
            
        return result
    
    def coalesce(self, value, default=None):
        """Get values from a collection without raising errors"""

        if value is None:
            return default
        
        return value

    def fetch_input_file_path_from_cli(self, cli_args):
        if len(cli_args) < 2 :
            raise CommandLineArgumentNotAvailable
        else:
            input_file_abs_path = cli_args[1]
            if not os.path.exists(input_file_abs_path):
                raise InvalidFilePath 
            
        return input_file_abs_path    
    
    def get_unique_iterable(self, iterable):  
        unique_iterable = []
        for item in  iterable:
            if not item in unique_iterable:
                unique_iterable.append(item)
        return unique_iterable
            

        