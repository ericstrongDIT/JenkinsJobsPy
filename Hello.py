from Person import Person

def printPerson(p):
    print(p)
    print(p.name)
    print(p.walk())


def main():
    eric = Person('Eric Strong')
    laura = Person('Laura Bermingham')

    printPerson(eric)
    printPerson(laura)

if __name__ == "__main__":
    main()