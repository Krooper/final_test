from Animals import Animal_class


class PackAnimal(Animal_class.Animal):
    def __init__(self, name, date_of_birth, _animal_type):
        super().__init__(name, date_of_birth)
        self._animal_type = 'Pack animal'

    def display(self):
        super().display()
        print("Type:", self._animal_type)
