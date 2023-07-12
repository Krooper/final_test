from Animals.Pets.Dog_class import Dog
from Registry_class import Registry


def main_menu(registry):
    working_reg = registry
    print("Main menu options:")
    print("1 - Show all animals in registry")
    print("2 - Add animal to registry")
    print("3 - Show commands of an animal")
    print("4 - Teach animal a new command")
    inp_com = input()

    try:
        inp_com = int(inp_com)
        if inp_com == 1:
            registry.show_animals()
            return main_menu(working_reg)
        elif inp_com == 2:
            registry.add_animal()
            return main_menu(working_reg)
        elif inp_com == 3:
            registry.show_animal_commands()
            return main_menu(working_reg)
        elif inp_com == 4:
            registry.add_command()
            return main_menu(working_reg)
        else:
            raise ValueError
    except ValueError:
        print('There is no such command! Try again!')
        return main_menu(working_reg)


def main():
    my_reg = Registry()
    main_menu(my_reg)


if __name__ == "__main__":
    main()
