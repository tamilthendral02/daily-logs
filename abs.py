from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def startengine(self):
        pass
class Bike(vehicle):
    def strat_engine(self):
        return "Engine started"
class car(vehicle):
    def strat_engine(self):
        return "Engine started"
    
c=Bike
d=car
print(c.strat_engine(1))
print(d.strat_engine(2))


