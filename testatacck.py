import hashlib
#fonction de hachage md5:
def calculate_md5(message):
    hasher = hashlib.md5()
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()


# Fonction pour charger le dictionnaire de mots de passe

def charger_dictionnaire(dictionnaire):
    try:
        with open(dictionnaire, 'rb') as fichier:
            mots_de_passe = fichier.read().decode('latin-1').splitlines()
            print("Dictionnaire chargé avec succès.")
        return mots_de_passe
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return []



def generate_variations(word):
    variations = set()  # Utiliser un ensemble pour éviter les doublons
    variations.add(word)  # Ajouter le mot d'origine

    replacements = {
        'a': ['@', '4', 'A'],
        'e': ['3', 'E'],
        'i': ['1', 'I'],
        'o': ['0', 'O'],
        's': ['$', '5', 'S'],
        't': ['7', 'T']
    }

    for i in range(len(word)):
        if word[i].lower() in replacements:
            for replacement in replacements[word[i].lower()]:
                new_word = word[:i] + replacement + word[i+1:]
                variations.add(new_word)  # Utiliser add() pour ajouter des éléments à un ensemble
    return list(variations)  # Convertir l'ensemble en liste pour respecter le format d'origine

# Charger le dictionnaire de mots de passe
dictionnaire = charger_dictionnaire("rockyou.txt")

# Créer une liste pour stocker toutes les variations de mots de passe
variations_totales = []
i=0

# Si le dictionnaire est chargé avec succès, générer des variations pour chaque mot de passe et les ajouter à la liste
if dictionnaire:
    for mot_de_passe in dictionnaire:
        print(i,": mot de passe actuel", mot_de_passe) 
        variations = generate_variations(mot_de_passe)
        print("les variation: ",variations)
        variations_totales.extend(variations)
        i=i+1
        



# Demander à l'utilisateur de saisir un hachage MD5
hachage_entre = input("Entrez le hachage MD5 à rechercher: ")

# Convertir les hachages MD5 dans le dictionnaire en un ensemble pour une recherche plus rapide
dictionnaire_hachages = set(calculate_md5(mot_de_passe) for mot_de_passe in dictionnaire)

# Initialiser une variable pour stocker le mot de passe correspondant
mot_de_passe_correspondant = None

# Parcourir le dictionnaire et chercher un mot de passe avec le même hachage MD5
for mot_de_passe in dictionnaire:
    if calculate_md5(mot_de_passe) == hachage_entre:
        mot_de_passe_correspondant = mot_de_passe
        break

# Si un mot de passe correspondant est trouvé, l'afficher
if mot_de_passe_correspondant:
    print("Un mot de passe qui a le même hachage MD5 est :", mot_de_passe_correspondant)
else:
    # Convertir les hachages MD5 dans la liste de variations en un ensemble pour une recherche plus rapide
    variations_hachages = set(calculate_md5(variation) for variation in variations_totales)
    
    # Parcourir les variations et chercher un hachage MD5 correspondant
    for variation, hachage in zip(variations_totales, variations_hachages):
        if hachage == hachage_entre:
            mot_de_passe_correspondant = variation
            break
            
    # Si un mot de passe correspondant est trouvé, l'afficher
    if mot_de_passe_correspondant:
        print("Un mot de passe qui a le même hachage MD5 est :", mot_de_passe_correspondant)
    else:
        print("Le mot de passe n'existe pas.")
