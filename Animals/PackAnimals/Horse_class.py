from Animals.PackAnimals.PackAnimal_class import PackAnimal


class Horse(PackAnimal):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self._commands = ['Neigh']
        self._subtype = "Horse"

    def display(self):
        super().display()
        print("Commands:")
        for command in self._commands:
            print(f"{command}")

    def get_subtype(self):
        return f"{self._subtype}({self._animal_type})"
