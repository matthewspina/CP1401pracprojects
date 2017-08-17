def main():
    name = get_name()
    number = int(input("how many letters?"))
    print_name(name, number)


def get_name():
    name = str(input("name?"))
    while len(name) == 0:
        print("name can not be blank")
        name = str(input("name?"))
    return name


def print_name(name, number):
    print(name[::number])


main()
