from abc import ABC,abstractmethod
class Birds(ABC):
    @abstractmethod
    def fly_sound(self):
        pass
class parrot(Birds):
    def fly_sound(self):
        return "happy environe"
class duck(Birds):
    def fly_sound(self):
        return "happy environe"
    
objs=[parrot(),duck()]
for obj in objs:
        print(obj.fly_sound)
    

def obj_behavior(d):
    return d.fly_sound()
print(obj_behavior(parrot()))
print(obj_behavior(duck()))


