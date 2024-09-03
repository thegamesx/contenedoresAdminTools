import random
import string


def generate_password():
    length = random.randint(12, 12)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password
