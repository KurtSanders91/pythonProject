import os
import random
import string


def random_string(length):
    return "absolutely random string"

class FooPrivate:
    def foo(self):
        pass

class Foo:
    def __init__(self):
        self.impl = FooPrivate()

    def foo(self):
        self.impl.foo()

def generate_random(n):
    name = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(n)])
    return name


def generate_name(length):
    name = generate_random(length)
    while os.path.isfile(name) and os.path.isdir(name):
        name = generate_random(length)
    return name