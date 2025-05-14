import random
import string

def generate_custom_id(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

print(generate_custom_id())