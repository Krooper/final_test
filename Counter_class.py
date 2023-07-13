from Registry_class import Registry


class Counter:
    def __init__(self, animal, counter):
        self.new_animal = animal
        self._counter = counter

    def __str__(self):
        return self._counter

    def add(self):
        self._counter += 1
        return self._counter

    def __enter__(self):
        return self.add()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.add()
        else:
            return False

