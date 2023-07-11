class Animal:
    def __init__(self, name, date_of_birth):
        self._name = name
        self._date_of_birth = date_of_birth

    def display(self):
        print("Name:", self._name)
        print("Date of birth:", self._date_of_birth)

    def get_name(self):
        return self._name


