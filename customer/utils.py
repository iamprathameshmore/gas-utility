import random
import string
import time

def reqid():
    current_time = time.gmtime()
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for n in range(4))
    data = f'#gasConnect-{random_string}-{current_time.tm_year}'
    return data

# Generate the random string and print it
# data = reqid()
# print(data)
