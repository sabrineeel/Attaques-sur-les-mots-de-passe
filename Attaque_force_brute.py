
import itertools
import hashlib

def calculate_md5(message):
    # Créez un objet hasher MD5
    hasher = hashlib.md5()
    
    # Mettez à jour le hasher avec le message
    hasher.update(message.encode('utf-8'))
    
    # Renvoie le hachage MD5 hexadécimal
    return hasher.hexdigest()

# Exemple d'utilisation
message = 'aa'
md5_hash = calculate_md5(message)

def generate_combinations(characters, length):
    combinations = []
    for i in range(1, length + 1):
        combinations.extend([''.join(combination) for combination in itertools.product(characters, repeat=i)])
    return combinations

def calculate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

# Liste des caractères
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Longueur maximale des combinaisons
max_length = 5  # Vous pouvez ajuster cette valeur selon vos besoins

# Valeur de hachage MD5 à comparer
h1 = md5_hash

# Générer les combinaisons
all_combinations = generate_combinations(characters, max_length)

# Comparer les combinaisons avec la valeur h1
for combination in all_combinations:
    md5_hash = calculate_md5(combination)
    if md5_hash == h1:
        print(f"La combinaison '{combination}' a produit le hachage MD5 identique à h1 : {h1}")
        break

