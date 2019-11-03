class Command:
    def __init__(self):
        self.items=[]

    def add(self,item):
        self.items.append(item)

    def execute(self):
        for item in self.items:



    def revert(self):
