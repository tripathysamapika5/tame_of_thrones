
class CircularArray:
    
    def __init__(self, iterable):
        
        self.length = len(iterable)
        self.circular_array = {}
        self.circular_array['element-to-index-mapping'] = {elem : index  for index, elem in enumerate(iterable)}
        self.circular_array['index-to-element-mapping'] = dict(enumerate(iterable))


    def read_element_clockwise(self, from_element, jump_to_pos):
        starting_pos = self.circular_array['element-to-index-mapping'].get(from_element) 
        destination_pos =  (starting_pos + jump_to_pos) % self.length
        
        return self.circular_array['index-to-element-mapping'].get(destination_pos)
        