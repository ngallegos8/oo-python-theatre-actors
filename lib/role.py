from .audition import Audition

class Role:
    
    all = []

    def __init__(self, character_name):
        self.character_name = character_name

    def audition(self):
        pass

    def actors(self):
        pass

    def locations(self):
        pass

    @classmethod
    def silver_screen(self):
        pass