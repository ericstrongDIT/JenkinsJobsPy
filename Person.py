

class Person:
    def __init__(self, name):
        self.name = name
    
    #person functions
    def walk(self):
        return (self.name + ' is walking')


    def __str__(self):
        return '{} has been created'.format(self.name)