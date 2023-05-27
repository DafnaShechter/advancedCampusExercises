class Dolphin:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


# Main program
dolphin1 = Dolphin("Dolly", 5)
dolphin2 = Dolphin("Doug", 3)

dolphin1.birthday()

print(dolphin1.get_age())
print(dolphin2.get_age())
