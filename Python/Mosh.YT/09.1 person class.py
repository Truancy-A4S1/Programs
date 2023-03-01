class Person:
    population_count = 0

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        Person.population_count += 1
    
    def get_full_name(self):
        return self.fname + " " + self.lname
    
    def get_age(self):
        return self.age
    
    def get_pop_id(self):
        return Person.population_count



p1 = Person("John","Smith", 34)
print(f'Person: {p1.get_full_name()}.. {p1.age} years old. PopID: {p1.get_pop_id()}')

p2 = Person("Mrary","Mehh", 33)
print(f'Person: {p2.get_full_name()}.. {p2.age} years old. PopID: {p2.get_pop_id()}')
