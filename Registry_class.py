class Registry:
    def __init__(self):
        self._animals = {'Pack animals': [], 'Pets': []}

    def add_animal(self, animal):
        if animal.get_type() == 'Pack animal':
            self._animals['Pack animals'].append(animal)
        elif animal.get_type() == 'Pet':
            self._animals['Pets'].append(animal)

    def pick_animal(self):
        print("Choose animal type:")
        for animal_type in self._animals.keys():
            print(f"{animal_type}")

        animal_type = input("Input: ")
        while animal_type not in self._animals.keys():
            print("No such animal type! Try again!\n")
            animal_type = input("Input: ")

        print("Choose animal:")
        for animal in self._animals[animal_type]:
            print(f"{animal.get_name()} - {animal.get_subtype()}")

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
