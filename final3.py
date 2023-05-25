import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_char, position):
        self.illegal_char = illegal_char
        self.position = position

    def __str__(self):
        return f"The username contains an illegal character '{self.illegal_char}' at position {self.position}."


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short. It must be at least 3 characters long."


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long. It must not exceed 16 characters."


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character."


class MissingCapitalLetter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class MissingSmallLetter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class MissingNumber(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class MissingSpecialCharacter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short. It must be at least 8 characters long."


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long. It must not exceed 40 characters."


def check_input(username, password):
    # Check username
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()
    if not all(c.isalnum() or c == '_' for c in username):
        illegal_char = next(c for c in username if not c.isalnum() and c != '_')
        position = username.index(illegal_char)
        raise UsernameContainsIllegalCharacter(illegal_char, position)

    # Check password
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()
    if not any(c.isupper() for c in password):
        raise MissingCapitalLetter()
    if not any(c.islower() for c in password):
        raise MissingSmallLetter()
    if not any(c.isdigit() for c in password):
        raise MissingNumber()
    if not any(c in string.punctuation for c in password):
        raise MissingSpecialCharacter()

    print("OK")


def main():
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        try:
            check_input(username, password)
            break
        except (UsernameTooShort, UsernameTooLong, UsernameContainsIllegalCharacter,
                PasswordTooShort, PasswordTooLong, MissingCapitalLetter,
                MissingSmallLetter, MissingNumber, MissingSpecialCharacter) as e:
            print(e)


if __name__ == "__main__":
    main()
