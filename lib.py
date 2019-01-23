import hashlib
import random
from random import randrange

def generate_challenge_string():
    symbols = '123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.SystemRandom().choice(symbols) for i in range(random.SystemRandom().randrange(10,99)))

def solve_challenge(string, difficulty):
    is_solved = False
    difficulty = ''.join('0' for i in range(difficulty))
    while is_solved == False:
        n = ''.join(random.SystemRandom().choice('123456789') for i in range(10))
        curr_string = string + str(n)
        curr_hash = hashlib.sha512(bytes(curr_string,"utf-8")).hexdigest()
        if curr_hash.startswith(difficulty):
            print(curr_hash)
            print(curr_string)
            is_solved = True
            return curr_string, curr_hash

def check_solution(string, solution_hash):
    checked_hash = hashlib.sha512(bytes(string,"utf-8")).hexdigest()
    if checked_hash == solution_hash:
        return True
    else:
        return False