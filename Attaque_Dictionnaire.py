#Fonction MD5 enn python
import hashlib

def calculate_md5(message):
    hasher = hashlib.md5()
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()



def charger_dictionnaire(rockyou):
    try:
        with open(rockyou, 'rb') as fichier:
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
dictionnaire = charger_dictionnaire("rockyou.txt")

# Convertir les hachages MD5 dans le dictionnaire en un ensemble pour une recherche plus rapide
dictionnaire_hachages = set(calculate_md5(mot_de_passe) for mot_de_passe in dictionnaire)


# Vérifier si le hachage MD5 du mot de passe entré est dans le dictionnaire des hachages
if hachage_entre in dictionnaire_hachages:
    print("Le mot de passe qui a le même hachage MD5 est :", mot_de_passe_entre)
else:
    print("Aucun mot de passe avec le même hachage MD5 n'a été trouvé dans le dictionnaire.")
