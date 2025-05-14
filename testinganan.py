import random
import string

#Code for random string for recit or reference for the reservation

def generate_custom_id(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

print(generate_custom_id())


def generate_custom_id(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))