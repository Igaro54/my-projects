from random import randint

def random_password():
    password = []
    for _ in range (0,16):
        password.append(chr(randint(33,126)))
    return "".join(password)

print(random_password())