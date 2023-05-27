class Dolphin:
    count_animals = 0

    def __init__(self, name="Lili"):
        self._name = name
        self._age = 0
        Dolphin.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name


# Main program
dolphin1 = Dolphin("Dolly")
dolphin2 = Dolphin()

print(dolphin1.get_name())
print(dolphin2.get_name())

dolphin1.set_name("Daisy")
print(dolphin1.get_name())

print(Dolphin.count_animals)
