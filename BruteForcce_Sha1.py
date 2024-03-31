import hashlib
import itertools



def calculate_sha1(message):
    hasher = hashlib.sha1()
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()



def generate_combinations(characters, length):
    combinations = []
    for i in range(1, length + 1):
        combinations.extend([''.join(combination) for combination in itertools.product(characters, repeat=i)])
    return combinations

h1 = input("Entrez le résultat de hachage SHA-1 : ")
password_length = int(input("Entrez la taille du mot de passe : "))


characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


all_combinations = []
for length in range(1, password_length + 1):
    all_combinations.extend(generate_combinations(characters, length))
# Comparer les combinaisons avec la valeur h1
password_found = False
for combination in all_combinations:
    sha1_hash = calculate_sha1(combination)
    if sha1_hash == h1:
        print(f"Le mot de passe est : {combination}")
        password_found = True
        break

if not password_found:
    print("Mot de passe non trouvé.")
