import Pet_class


class Hamster(Pet_class.Pet):
    def __init__(self, name, date_of_birth, animal_type, _commands):
        super().__init__(name, date_of_birth, animal_type)
        self._commands = ['Hiss']

    def display(self):
        super().display()
        print("Commands:\n")
        for command in self._commands:
            print(f"{command}\n")
