# 1. Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person): 
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

# 2. Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)
        Job.__init__(self, salary)            

# 3. Multilevel Inheritance
class Manager(EmployeePersonJob):  
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self, name, salary)  
        self.department = department

# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(self, name, salary)  
        self.team_size = team_size

# 5. Hybrid Inheritance (Multiple + Multilevel)
class SeniorManager(Manager, AssistantManager):  
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)        
        AssistantManager.__init__(self, name, salary, team_size)  