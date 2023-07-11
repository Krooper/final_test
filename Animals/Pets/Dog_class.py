import Pet_class


class Dog(Pet_class.Pet):
    def __init__(self, name, date_of_birth, animal_type, _commands):
        super().__init__(name, date_of_birth, animal_type)
        self._commands = ['Bark']

    def display(self):
        super().display()
        print("Commands:\n")
        for command in self._commands:
            print(f"{command}\n")
