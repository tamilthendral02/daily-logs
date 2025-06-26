class parent:
    def __init__(self, name, dob):
        self._name = name
        self._dob = dob

class sub(parent):
    def func(self):
        return self._name, self._dob

p = sub("thendral", "17")
print(p.func())
