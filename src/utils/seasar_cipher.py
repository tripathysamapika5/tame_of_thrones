
from src.utils.datatype import CircularArray
from src.utils.utils import Utilities

class SeasarCipher:
    
    def __init__(self):
        self.utility = Utilities()
        self.circular_array = CircularArray(self.utility.get_all_alphabets())
    
    def encode(self, input_string):
        secret_key = len(input_string)
        encoded_string = ''
        for char in input_string:
            encoded_string = encoded_string + self.circular_array.read_element_clockwise(char, secret_key)
            
        return encoded_string
    
    def is_valid_encoding(self, original_string, encoded_string_tocompare):
        encoded_string = self.encode(original_string) 
        
        input_counter = self.utility.iterable_item_counter(encoded_string_tocompare)
        encoded_string_counter = self.utility.iterable_item_counter(encoded_string)
        
        
        for key in encoded_string_counter:
            if self.utility.coalesce(input_counter.get(key),0) < self.utility.coalesce(encoded_string_counter.get(key),0):
                return False
            
        return True
        
            
        
    