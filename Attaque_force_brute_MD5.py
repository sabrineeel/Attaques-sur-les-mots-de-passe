
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

def validate_md5_hash(md5_hash):
    # Vérifie que la longueur du hachage MD5 correspond à 32 caractères hexadécimaux
    return re.match(r"^[a-fA-F0-9]{32}$", md5_hash) is not None

def validate_password_length(password_length):
    # Vérifie que la taille du mot de passe est un entier positif
    return password_length.isdigit() and int(password_length) > 0

while True:
    h1 = input("Entrez le résultat de hachage MD5 : ")
    if validate_md5_hash(h1):
        break
    else:
        print("Le hachage MD5 entré n'est pas valide. Assurez-vous qu'il s'agit d'un hachage MD5 de 32 caractères hexadécimaux.")

while True:
    password_length = input("Entrez la taille du mot de passe : ")
    if validate_password_length(password_length):
        password_length = int(password_length)  # Convertir en entier
        break
    else:
        print("La taille du mot de passe entrée n'est pas valide. Assurez-vous qu'elle est un entier positif.")
def calculate_md5(message):
    hasher = hashlib.md5()
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()

def generate_combinations(characters, length):
    combinations = []
    for i in range(1, length + 1):
        combinations.extend([''.join(combination) for combination in itertools.product(characters, repeat=i)])
    return combinations



# Liste des caractères
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Générer les combinaisons
all_combinations = []
for length in range(1, password_length + 1):
    all_combinations.extend(generate_combinations(characters, length))

# Comparer les combinaisons avec la valeur h1
password_found = False
for combination in all_combinations:
    md5_hash = calculate_md5(combination)
    if md5_hash == h1:
        print(f"Le mot de passe est : {combination}")
        password_found = True
        break

if not password_found:
    print("Mot de passe non trouvé.")
