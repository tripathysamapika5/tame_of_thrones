from src.message.message import Message

class Message_Validation_Util:
    def __init__(self, utility):
       self.utility = utility
    
    def find_valid_kingdoms_from_input_file (self, input_file_abs_path):
        lines = self.utility.read_file_to_list_of_lines(input_file_abs_path)
        valid_kingdoms_list = []
        
        for line in lines:
            kingdom, message = line.split(" ")[0], " ".join(line.split(" ")[1:]).lower()
            message_obj = Message(kingdom, message)
            
            emblame = self.utility.get_kingdom_to_emblame_mapping().get(kingdom.upper())
            
            if message_obj.is_valid():
                valid_kingdoms_list.append(kingdom)
                
        #get the unique kingdome names
        unique_valid_kingdoms = self.utility.get_unique_iterable(valid_kingdoms_list)
        
        # Check the allias it got
        if len(unique_valid_kingdoms) >= 3:
            unique_valid_kingdoms.insert(0, self.utility.get_message_sender_name())
            valid_kingdoms = " ".join(unique_valid_kingdoms)
        else:
            valid_kingdoms = None
        
        return valid_kingdoms
