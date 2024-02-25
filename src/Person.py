class Person():

    def __init__(self,name,family):
        self.name = name
        self.family = family

    def to_dict(self):
        return {'name': self.name, 'family': self.family}



    
        
    