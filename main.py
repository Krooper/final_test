from Registry_class import Registry
from Counter_class import Counter


def main_menu(registry, counter):

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
            return main_menu(working_reg, counter)
        elif inp_com == 2:
            new_animal = registry.add_animal()
            with Counter(new_animal, counter) as new_counter:
                if new_animal.get_name() == "":
                    raise AttributeError("Empty name!")
                else:
                    counter = new_counter
                    print(f"Animal number: {counter}")
            return main_menu(working_reg, counter)
        elif inp_com == 3:
            registry.show_animal_commands()
            return main_menu(working_reg, counter)
        elif inp_com == 4:
            registry.add_command()
            return main_menu(working_reg, counter)
        else:
            raise ValueError
    except ValueError:
        print('There is no such command! Try again!')
        return main_menu(working_reg, counter)


def main():
    counter = 0
    my_reg = Registry()
    main_menu(my_reg, counter)


if __name__ == "__main__":
    main()
