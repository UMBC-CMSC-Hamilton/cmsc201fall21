"""
    There is a keyword called "class"

    We can make our own data types

        We can make something called "Animal" and it has data and it has functions (class methods)

"""

A_CONSTANT = 4

class Animal:
    def __init__(self, wb, species, noise):
        """
            Constructor - method that runs when a class is created
            
            self. tells the class that this a variable that is contained within that class
        """
        self.warm_blooded = wb
        self.species = species
        self.noise = noise
    
    def eat(self, food):
        print(f'The {self.species} has eaten {food}')
    
    def make_noise(self):
        # the reason that "self" is passed as the first parameter is a way to give you access
        # to the rest of the classes member variables.
        print(f'The {self.species} says {self.noise}')


a = Animal(True, 'dog', 'woof')
a.make_noise()
# make_noise(a)
a.eat('kibbles')

"""
    Kind of like a dictionary except "better"
"""

student_record = {'name': 'Eric', 'ID': 'eric8', 'gpa': 3.5}
print(student_record['name'])


class Student:
    def __init__(self, student_name, student_id):
        self.name = student_name
        self.id = student_id
        self.gpa = 0
        # don't mess with me, the class will handle it
        self.__courses = []
    
    def take_course(self, the_class, grade):
        self.__courses.append([the_class, grade])
        print(f'We have added {the_class} to {self.name}\'s transcript')
    
    def calculate_gpa(self):
        grade_equivalents = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        total = 0
        for course, grade in self.__courses:
            print(course, grade)
            total += grade_equivalents[grade.upper()]
            
        # all classes are equal credits
        self.gpa = total / len(self.__courses)
        return self.gpa
    
eric_the_student = Student('Eric', 'eric8')
eric_the_student.take_course('cmsc201', 'C')
eric_the_student.take_course('math151', 'A')
eric_the_student.take_course('phys121', 'B')
eric_the_student.take_course('phil100', 'A')
eric_the_student.take_course('ancs100', 'B')

print(eric_the_student.calculate_gpa())
# eric_the_student.courses.append('hi this is bad')
# print(eric_the_student.calculate_gpa())


class Movie:
    def __init__(self):
        """
            You SHOULD declare all variables up here in __init__
        """
        self.movie_name = ''
    
    def make_new_var(self):
        self.movie_name = 'The Fifth Element'
    
    def print_movie_name(self):
        print(self.movie_name)


m = Movie()
# m.make_new_var()
m.print_movie_name()


class Number:
    def __init__(self, value):
        self.value = value
        
    def __add__(self, other):
        """
            Operator overloading
        """
        print('I am being called', other.value)
        return self.value + other.value
    
    def __repr__(self):
        return str(self.value)


# an instance of Number five.value = 5
five = Number(5)
# an instance of Number, a specific number class with its own variables seven.value = 7
seven = Number(7)
print(five + seven)
# five.__add__(seven)

"""
    Just like lists, dictionaries, classes are also mutable

        You can modify elements within the class when you pass a class to a function
"""

def set_number_to_17(the_num):
    the_num.value = 17


x = Number(3)
set_number_to_17(x)
print(x)


"""
    Important bits about classes:
        They have methods and variables
        In python we declare the "member variables" in the constructor
        
        Create new methods (function inside of a class)
        Advantage = we get to use the data that the class stores

        In python they are MUTABLE / pass by reference (functions can modify them)
        
    Disadvantages of classes:
        adding a bit of complexity
    
    Weird stuff:
        operator overloading = redefine things like the plus sign, minus, sign
        
        
"""


class Ship:
    def __init__(self, name, length, metal_or_wood, ):
        self.name = name
        self.length = length
        self.metal_or_wood = metal_or_wood
        self.sunk = False
        
    def sink_ship(the_ship):
        the_ship.sunk = True
        
    def fight_ship(self, other_ship):
        print(f'{self.name} is fighting {other_ship.name}')


s1 = Ship('HMS Victory', 50, 'wood')
s2 = Ship('RMS Titanic', 300, 'steel')
s3 = Ship('USS Maine', 120, 'steel')

s1.fight_ship(s3)
# Ship.fight_ship(s1, s3)
s2.fight_ship(s3)

s1.sink_ship()
s2.sink_ship()
#s2.sink_ship() --> Ship.sink_ship(s2)
print(s1.sunk)
