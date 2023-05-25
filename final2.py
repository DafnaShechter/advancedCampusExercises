class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self.name_ = name
        self.hunger_ = hunger

    def get_name(self):
        return self.name_

    def is_hungry(self):
        return self.hunger_ > 0

    def feed(self):
        if self.hunger_ > 0:
            self.hunger_ -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("Meow")

    def chase_laser(self):
        print("Meeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._stink_count = 6

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear Lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._color = "Green"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    # Feed the hungry animals
    for animal in zoo_lst:
        while animal.is_hungry():
            print(animal.__class__.__name__)
            animal.feed()

    # Interact with the animals
    for animal in zoo_lst:
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
