from Animals.Pets.Dog_class import Dog
from Registry_class import Registry


def main():
    dog1 = Dog("Ivy", "2020-05-18")
    my_reg = Registry()
    my_reg.add_animal(dog1)
    animal = my_reg.pick_animal()
    animal.display()


if __name__ == "__main__":
    main()
