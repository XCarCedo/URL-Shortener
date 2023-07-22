import random
import string

def generate_id(chars: str = string.ascii_lowercase + string.ascii_uppercase + string.digits,
	lenght: int = 10):
	return "".join([random.choice(chars) for _ in range(lenght)])

print(generate_id())