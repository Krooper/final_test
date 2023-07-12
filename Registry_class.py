from Animals.PackAnimals.Horse_class import Horse
from Animals.PackAnimals.Donkey_class import Donkey
from Animals.Pets.Dog_class import Dog
from Animals.Pets.Cat_class import Cat
from Animals.Pets.Hamster_class import Hamster
import time


def date_check():
    date = input('Input its date of birth (yyyy-mm-dd): ')
    try:
        valid_date = time.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Invalid date! Try again!')
        return date_check()
    return valid_date


class Registry:
    def __init__(self):
        self._animals = {'Pack animals': [], 'Pets': []}
        self._subtypes = {'Pack animals': ["Horse", "Donkey"], 'Pets': ["Dog", "Cat", "Hamster"]}

    def show_types(self):
        for animal_type in self._animals.keys():
            print(animal_type)

    def show_subtypes(self, animal_type):
        subtype_set = set()
        for subtype in self._subtypes[animal_type]:
            subtype_set.add(subtype)

        for subtype in subtype_set:
            print(subtype)
        return subtype_set

    def show_animals_by_type(self, animal_type):
        for animal in self._animals[animal_type]:
            print(f"{animal.get_name()} - {animal.get_subtype()}")

    def show_animals(self):
        for animal_type in self._animals.keys():
            print(animal_type)
            self.show_animals_by_type(animal_type)

    def pick_type(self):
        animal_type = input("Input: ")
        while animal_type not in self._animals.keys():
            print("No such animal type! Try again!\n")
            animal_type = input("Input: ")
        return animal_type

    def pick_subtype(self, subtype_set):
        animal_subtype = input("Input: ")
        while animal_subtype not in subtype_set:
            print("No such animal subtype! Try again!\n")
            animal_subtype = input("Input: ")
        return animal_subtype

    def add_animal(self):
        name = input("Input a name for a new animal: ")
        date_of_birth = date_check()

        print("Choose animal type: ")
        self.show_types()
        animal_type = self.pick_type()

        if animal_type == 'Pack animal':
            subtypes = self.show_subtypes(animal_type)
            animal_subtype = self.pick_subtype(subtypes)

            if animal_subtype == "Horse":
                new_animal = Horse(name, date_of_birth)
            else:
                new_animal = Donkey(name, date_of_birth)
        else:
            subtypes = self.show_subtypes(animal_type)
            animal_subtype = self.pick_subtype(subtypes)
            if animal_subtype == "Dog":
                new_animal = Dog(name, date_of_birth)
            elif animal_subtype == "Cat":
                new_animal = Cat(name, date_of_birth)
            else:
                new_animal = Hamster(name, date_of_birth)

        self._animals[animal_type].append(new_animal)

    def pick_animal(self):
        print("Choose animal type:")
        self.show_types()
        animal_type = self.pick_type()

        print("Choose animal:")
        self.show_animals_by_type(animal_type)
        animal_names = []
        for animal in self._animals[animal_type]:
            animal_names.append(animal.get_name())

        animal_name = input("Input: ")
        while animal_name not in animal_names:
            print("No such animal! Try again!\n")
            animal_name = input("Input: ")

        for animal in self._animals[animal_type]:
            if animal_name == animal.get_name():
                return animal

    def show_animal_commands(self):
        animal = self.pick_animal()
        animal.show_commands()

    def add_command(self):
        animal = self.pick_animal()
        new_command = input("Input a new command for animal: ")
        animal.add_command(new_command)
