# Task 1
# Create a class method named validate, which should be called from the __init__ method to validate parameter email,
# passed to the constructor. The logic inside the validate method could be to check if the passed email parameter is
# a valid email string.
# Email validations:
# Valid email address format
# Wiki: Email address

class Validate:
    def __init__(self, email) -> None:
        self.email = email
        Validate.validate(email)

    def validate(email: str) -> None:
        email_parts = email.split("@")
        if len(email_parts) != 2:
            raise ValueError("Invalid email")

        printable_characters = ".!#$%&'*+-/=?^_`{|}~"
        local_part = email_parts[0]
        domain_part = email_parts[1]

        if local_part[0] in printable_characters:
            raise ValueError(
                f"The symbol '{local_part[0]}' is at the beginning of the string, so it is an invalid email address")
        if local_part[len(local_part) - 1] in printable_characters:
            raise ValueError(
                f"The symbol '{local_part[0]}' is at the end of the string, so it is an invalid email address")

        not_allowed_domain_characters = "!#$%&'*+/=?^_`{|}~"

        if domain_part[0] in not_allowed_domain_characters:
            raise ValueError(f"The symbol '{domain_part[0]}' is not a valid for domain part of the email address")
        if domain_part[0] in ".-":
            raise ValueError(
                f"The symbol '{domain_part[0]}' is at the beginning of the string, so it is an invalid email address")
        if domain_part[len(domain_part) - 1] in ".-":
            raise ValueError(
                f"The symbol '{domain_part[0]}' is at the end of the string, so it is an invalid email address")
        if ".." in email:
            raise ValueError("The symbol '..' is not allowed, so it is not a valid email address")


a = Validate("kokos@com.ua")
Validate.validate("brave@com.ua")

try:
    Validate.validate("star@@com.ua")
except ValueError as e:
    assert f"{e}" == "Invalid email"
else:
    assert False, "Email should not be valid"

try:
    Validate.validate("star.com.ua")
except ValueError as e:
    assert f"{e}" == "Invalid email"
else:
    assert False, "Email should not be valid"

try:
    Validate.validate(".star@com.ua")
except ValueError as e:
    assert f"{e}" == "The symbol '.' is at the beginning of the string, so it is an invalid email address"
else:
    assert False, "Email should not be valid"

try:
    Validate.validate("star..good@com.ua")
except ValueError as e:
    assert f"{e}" == "The symbol '..' is not allowed, so it is not a valid email address"
else:
    assert False, "Email should not be valid"
