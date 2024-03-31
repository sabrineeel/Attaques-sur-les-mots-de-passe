print (""" 

██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████                                                            
                 
""")
import hashlib
import itertools
import re

def calculate_sha1(message):
    hasher = hashlib.sha1()
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()

def validate_sha1_hash(md5_hash):
    # Vérifie que la longueur du hachage MD5 correspond à 32 caractères hexadécimaux
    return re.match(r"^[a-fA-F0-9]{40}$", md5_hash) is not None

def validate_password_length(password_length):
    # Vérifie que la taille du mot de passe est un entier positif
    return password_length.isdigit() and int(password_length) > 0


while True:
    h1 = input("Entrez le résultat de hachage Sha1 : ")
    if validate_sha1_hash(h1):
        break
    else:
        print("Le hachage sha1 entré n'est pas valide. Assurez-vous qu'il s'agit d'un hachage Sha1 de 40 caractères hexadécimaux.")

while True:
    password_length = input("Entrez la taille du mot de passe : ")
    if validate_password_length(password_length):
        password_length = int(password_length)  # Convertir en entier
        break
    else:
        print("La taille du mot de passe entrée n'est pas valide. Assurez-vous qu'elle est un entier positif.")




def generate_combinations(characters, length):
    combinations = []
    for i in range(1, length + 1):
        combinations.extend([''.join(combination) for combination in itertools.product(characters, repeat=i)])
    return combinations




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
