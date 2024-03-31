
print (""" 

██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████                                                            
                 

""")
import itertools
import hashlib

def calculate_md5(message):
    # Créez un objet hasher MD5
    hasher = hashlib.md5()
    
    # Mettez à jour le hasher avec le message
    hasher.update(message.encode('utf-8'))
    
    # Renvoie le hachage MD5 hexadécimal
    return hasher.hexdigest()

def generate_combinations(characters, length):
    combinations = []
    for i in range(1, length + 1):
        combinations.extend([''.join(combination) for combination in itertools.product(characters, repeat=i)])
    return combinations

# Demander à l'utilisateur d'entrer le résultat de hachage MD5 et la taille du mot de passe
h1 = input("Entrez le résultat de hachage MD5 : ")
password_length = int(input("Entrez la taille du mot de passe : "))

# Liste des caractères
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Générer les combinaisons
all_combinations = generate_combinations(characters, password_length)

# Comparer les combinaisons avec la valeur h1
for combination in all_combinations:
    md5_hash = calculate_md5(combination)
    if md5_hash == h1:
        print(f"Le mot de passe est : {combination}")
        break
else:
    print("Mot de passe non trouvé.")
