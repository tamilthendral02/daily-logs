

class parent:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

class child(parent):
    def func(self):
        return self.name, self.dob

p = child("thendral", "17")
print(p.func())
