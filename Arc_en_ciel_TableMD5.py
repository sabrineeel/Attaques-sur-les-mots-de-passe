import itertools
import hashlib
import os

def generate_rainbow_table(charset, min_length, max_length, filename):
    with open(filename, 'w') as f:
        for r in range(min_length, max_length + 1):
            for password in itertools.product(charset, repeat=r):
                password = ''.join(password)
                hash_value = hashlib.md5(password.encode()).hexdigest()
                f.write(f"{hash_value}:{password}\n")

generate_rainbow_table('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',1,4, "table.txt")
