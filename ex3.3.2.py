class UnderAge(Exception):
    def __str__(self):
        return "Your age is less than 18. You are under age."


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


# Test the function
send_invitation("Dafna", 17)
send_invitation("Adam", 20)
