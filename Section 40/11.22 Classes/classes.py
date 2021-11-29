"""

    Classes - what are they?
    
        it allows you to create functions (methods) and data that the methods operate on

        Records in a filing cabinet
"""


class Student:
    def __init__(self, name, uid):
        """
            Constructor = it's called when you declare the class

        """
        self.name = name
        self.uid = uid
        self.classes = []
    
    def add_class(self, the_class, grade):
        """
        :param the_class: string which is the class name
        :param grade: string with A, B, C, D, F
        """
        self.classes.append([the_class, grade])
        print(f'{the_class} has been added to {self.name}\'s transcript')
        
    def calculate_gpa(self):
        print('Calculating', self.name, 'gpa')
        grade_equivalents = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        total = 0
        for the_course, the_grade in self.classes:
            total += grade_equivalents[the_grade]
        
        return total / len(self.classes)


# this calls the student constructor
#
eric = Student('Eric', 'eric8')
eric.add_class('cmsc201', 'A')
eric.add_class('math151', 'B')
eric.add_class('math221', 'A')
eric.add_class('gwst100', 'B')
eric.add_class('phys121', 'C')
print(eric.calculate_gpa())
# the secret:
# Student.calculate_gpa(eric)


jimmy = Student('James', 'james1')
jimmy.add_class('musc100', 'A')
jimmy.add_class('stat451', 'C')
jimmy.add_class('poli100', 'B')
jimmy.add_class('econ102', 'A')
jimmy.add_class('cmsc341', 'A')

print(jimmy.calculate_gpa())
becca = Student('Becca', 'bc2')
"""
    Each of these different students are considered "instances of the Student Class"
"""
print(eric.name, eric.uid)


class Song:
    def __init__(self, title, singer, length, genre):
        self.title = title
        self.length = length
        self.genre = genre
        self.singer = singer
        
    def skip(self):
        pass
    
    def play(self):
        print(f'Now playing ... {self.title} by {self.singer}')
    

four_thirty_three = Song('4:33', 'John Cage', 4*60 + 33, 'pop-experimental')
the_pie_song = Song('American Pie', 'Don McLean', 8 * 60, 'americana')
fdo = Song('First Day Out','T. Grisly', 2 * 60 + 45, 'rap')
# Songs are basically like dictionaries, but the advantage is that you can make methods that go along with it.
some_song = {'name': 'Summer', 'artist': 'Vivaldi', 'time': 8 * 60, 'genre': 'classical'}
song_list = [four_thirty_three, the_pie_song, fdo]
for song in song_list:
    song.play()
    

class Animal:
    def __init__(self, species):
        self.species = species
        self.sleep_time = 0
        self.awake = True
        
    def eat(self, food):
        print(self.species, 'is eating', food)

    def sleep(self, time):
        self.awake = False
        self.sleep_time += time
    
    def awake(self):
        self.awake = True
        
    def play(self, other_animal):
        print(self.species, 'is playing with', other_animal.species)
        
        

the_lion = Animal('Lion')
the_lion.eat('snack')

dog = Animal('Pupper')
the_lion.play(dog)
dog.play(the_lion)
print(dog.species)
print(the_lion.species)


class VoteSystem:
    def __init__(self):
        self.ballots = []
        
    def count_ballots(self):
        count_dict = {}
        for ballot in self.ballots:
            if ballot in count_dict:
                count_dict[ballot] += 1
            else:
                count_dict[ballot] = 1
        return count_dict
    
    def vote(self, candidate_name):
        self.ballots.append(candidate_name)

vs = VoteSystem()
vs.vote('Elon Musk')

vs.vote('Elon Musk')

vs.vote('Elon Musk')

vs.vote('Elon Musk')

vs.vote('Elon Musk')


vs.vote('Jeff Bezos')
vs.vote('Jeff Bezos')
vs.vote('Jeff Bezos')

vs.vote('Lex Luthor')
vs.vote('Lex Luthor')
vs.vote('Lex Luthor')
vs.vote('Lex Luthor')
vs.vote('Lex Luthor')
vs.vote('Lex Luthor')
vs.vote('Lex Luthor')
vs.vote('Lex Luthor')
vs.vote('Lex Luthor')
for i in range(10000):
    vs.ballots.append('Eric Hamilton')

print(vs.count_ballots())


class Ship:
    def __init__(self, name, length, propulsion):
        self.name = name
        self.length = length
        self.propulsion = propulsion
        
    def battle(self, other_ship):
        print(self.name, 'is battling', other_ship.name)


titanic = Ship('RMS Titanic', 320, 'triple expansion steam engine')
black_pearl = Ship('Black Pearl', 40, 'sail or magic')
the_victory = Ship('HMS Victory', 55, 'sail')
the_maine = Ship('USS Maine', 60, 'steam')
the_victory.battle(titanic)


class Car:
    def __init__(self, make, model, year, color, interior):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.interior = interior
        self.owner = ''
        self.mileage = 0

    def buy(self, new_owner):
        self.owner = new_owner
        
    def drive(self, miles):
        self.mileage += miles
    
    def repaint(self, new_color):
        self.color = new_color

