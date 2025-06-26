class parent:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob
        
    def func(self):
            return self.__name,self.__dob
        
a=parent("thendral",17)
print(a.func())
