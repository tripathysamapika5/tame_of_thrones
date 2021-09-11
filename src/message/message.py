from src.utils.utils import Utilities
from src.utils.seasar_cipher import SeasarCipher

class Message:
    
    def __init__(self, kingdom, message):
        self.kingdom = kingdom
        self.message = message
        self.kingdom_to_emblame_mapping = Utilities().get_kingdom_to_emblame_mapping()
        
    def is_valid(self):
        emblame = self.kingdom_to_emblame_mapping.get(self.kingdom.upper())
        return  SeasarCipher().is_valid_encoding(emblame, self.message)