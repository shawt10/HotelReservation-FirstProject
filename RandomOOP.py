import random
import string

class OPFUN:
    @staticmethod
    def generate_custom_id(length=8):  # Ensure length is correctly defined
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choices(chars, k=length))
