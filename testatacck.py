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
dictionnaire = charger_dictionnaire("dic.txt")

# Créer une liste pour stocker toutes les variations de mots de passe
variations_totales = []


# Si le dictionnaire est chargé avec succès, générer des variations pour chaque mot de passe et les ajouter à la liste
if dictionnaire:
    for mot_de_passe in dictionnaire:
       
        variations = generate_variations(mot_de_passe)
        
        variations_totales.extend(variations)
       
        


# Demander à l'utilisateur de saisir un hachage MD5
hachage_entre = input("Entrez le hachage MD5 à rechercher: ")

# Initialiser une variable pour stocker le mot de passe correspondant
mot_de_passe_correspondant = None

# Convertir les hachages MD5 dans le dictionnaire en un ensemble pour une recherche plus rapide
dictionnaire_hachages = set(calculate_md5(mot_de_passe) for mot_de_passe in dictionnaire)

# Parcourir le dictionnaire et chercher un mot de passe avec le même hachage MD5
for mot_de_passe in dictionnaire:
    if calculate_md5(mot_de_passe) == hachage_entre:
        mot_de_passe_correspondant = mot_de_passe
        break

# Si un mot de passe correspondant est trouvé dans le dictionnaire, afficher le mot de passe
if mot_de_passe_correspondant:
    print("Un mot de passe qui a le même hachage MD5 est :", mot_de_passe_correspondant)
else:
 # Convertir les hachages MD5 dans la liste de variations en un ensemble pour une recherche plus rapide
 variations_hachages = []

 for mot_de_passe in variations_totales:
    hachage = calculate_md5(mot_de_passe)  # Calculer le hachage MD5
    variations_hachages.append(hachage)  # Ajouter le hachage à la liste variations_hachages

# Rechercher le hachage MD5 entré par l'utilisateur dans la liste des hachages des variations
 if hachage_entre in variations_hachages:
    index = variations_hachages.index(hachage_entre)
    mot_de_passe_correspondant = variations_totales[index]
    print("Un mot de passe qui a le même hachage MD5 est :", mot_de_passe_correspondant)
 else:
    print("Le mot de passe n'existe pas.")
