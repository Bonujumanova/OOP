from string import ascii_lowercase
from random import randint, choices

class EmailValidator:

    acceptable_chars: str = ascii_lowercase + " ".join(list(map(str, range(10)))) + "." + "@" + "_"

    def __init__(self):
        pass

    @classmethod
    def get_random_email(cls):
        acceptable_chars: str = ascii_lowercase + "".join(list(map(str, range(10)))) + "_"
        len_email: int = randint(8, 100)
        email = "".join(choices(acceptable_chars, k=len_email)) + "@gmail.com"

        return email



    @classmethod
    def check_email(cls, email):

        is_str: bool = cls.is_email_str(email)

        if is_str:
            dog_index: int = email.find("@")

            if email.count(".") <= 2 and email.count("@") == 1:
                if email.find(".") + 1 == email.rfind("."):
                    return False
                elif email.find("@") < email.rfind(".") :
                    if len(email[:dog_index]) <= 100 and len(email[dog_index:]) <= 50:
                        for char in email:
                            if char not in cls.acceptable_chars:
                                return False
                        else:
                            return True
        return False


    @staticmethod
    def is_email_str(email):
       return isinstance(email, str)



res = EmailValidator().check_email("@")
print(res)
print(EmailValidator.get_random_email())