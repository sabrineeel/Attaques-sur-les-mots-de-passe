#Fonction MD5 enn python
import hashlib

def calculate_md5(message):
    hasher = hashlib.md5()
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()



def charger_dictionnaire(dictionnaire):
    try:
        with open(dictionnaire, 'rb') as fichier:
            mots_de_passe = fichier.read().decode('latin-1').splitlines()
            print("Dictionnaire chargé avec succès.")
        return mots_de_passe
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return []




# Demander à l'utilisateur de saisir un mot de passe à rechercher
mot_de_passe_entre = input("Entrez votre mot de passe: ")

# Calculer le hachage MD5 du mot de passe entré par l'utilisateur
hachage_entre = calculate_md5(mot_de_passe_entre)

print("le hacahge de ce mot de pass est: " +hachage_entre)



# Charger le dictionnaire de mots de passe
dictionnaire = charger_dictionnaire("dictionnaire.txt")

# Convertir les hachages MD5 dans le dictionnaire en un ensemble pour une recherche plus rapide
dictionnaire_hachages = set(calculate_md5(mot_de_passe) for mot_de_passe in dictionnaire)

# Initialiser une variable pour stocker le mot de passe correspondant
mot_de_passe_correspondant = None

# Parcourir le dictionnaire et chercher un mot de passe avec le même hachage MD5
index = 0
while mot_de_passe_correspondant is None and index < len(dictionnaire):
    if calculate_md5(dictionnaire[index]) == hachage_entre:
        mot_de_passe_correspondant = dictionnaire[index]
    else:
        index += 1

# Si un mot de passe correspondant est trouvé, l'afficher
if mot_de_passe_correspondant:
    print("Un mot de passe qui a le même hachage MD5 est :", mot_de_passe_correspondant)
else:
    print("Aucun mot de passe avec le même hachage MD5 n'a été trouvé dans le dictionnaire.")
