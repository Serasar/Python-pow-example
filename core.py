import hashlib
import random
import time

def calculate_pow(challenge_string, difficulty)
string = "Hsafgasdfsadfsafsfsdf"
complete = False
while complete == False:
    n = ''.join(random.SystemRandom().choice('123456789') for i in range(10))
    curr_string = string + str(n)
    curr_hash = hashlib.sha512(bytes(curr_string,"utf-8")).hexdigest()
    if curr_hash.startswith('000'):
        print(curr_hash)
        print(curr_string)
        complete = True