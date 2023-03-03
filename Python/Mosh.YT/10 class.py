class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        return (f"{self.name} is talking...")


Rand = Person("Rand Althor")

print(f'Name: {Rand.name}')
print(f'Talk: {Rand.talk()}')


# 03:20:00 MODULES
# Import specific functions from the module and call it without calling the module name
from utils_module import find_max
print(find_max([1, 2, 9, 4, 5]))

# Import all the function from the module and call it after the module name
import utils_module
print(utils_module.find_max([1, 2, 9, 4, 5]))

