import configparser
import os 
import string


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
