#Fonction MD5 enn python
import hashlib

def calculate_md5(message):
    hasher = hashlib.md5()
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()

# Demander à l'utilisateur de saisir un mot de passe à rechercher
mot_de_passe_entre = input("Entrez votre mot de passe: ")

# Calculer le hachage MD5 du mot de passe entré par l'utilisateur
hachage_entre = calculate_md5(mot_de_passe_entre)
print("le hachage est: " + hachage_entre)

