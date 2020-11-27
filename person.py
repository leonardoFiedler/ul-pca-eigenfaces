class Person:
    
    def __init__(self, id, label, data):
        self.id = id
        self.label = label
        self.data = data
    
    def to_string(self):
        print(f'Person [id = {self.id}, label = {self.label}, data = {self.data}]')