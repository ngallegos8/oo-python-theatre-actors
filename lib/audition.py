
class Audition:
    
    all = []

    def __init__(self, location, hired):
        self.location = location
        self.hired = hired
        Audition.all.append(self)

    def role(self):
        pass

    def actor(self):
        pass

    def call_back(self):
        pass