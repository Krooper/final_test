from Animals import Animal_class


class Pet(Animal_class.Animal):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self._animal_type = 'Pet'

    def display(self):
        super().display()
        print("Type:", self._animal_type)

    def get_type(self):
        return self._animal_type
