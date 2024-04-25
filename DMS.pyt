import tkinter as tk
from tkinter import messagebox
import hashlib

def charger_dictionnaire(rockyou):
    try:
        with open(rockyou, 'rb') as fichier:
            mots_de_passe = fichier.read().decode('latin-1').splitlines()
            return mots_de_passe
    except FileNotFoundError:
        return []

def rechercher_mot_de_passe(algo):
    hachage_entre = hash_entry.get()

    # Sélection de l'algorithme de hachage
    if algo == "MD5":
        hash_func = hashlib.md5
    elif algo == "SHA-1":
        hash_func = hashlib.sha1
    elif algo == "SHA-256":
        hash_func = hashlib.sha256
    elif algo == "SHA-3":
        hash_func = hashlib.sha3_256
    else:
        messagebox.showerror("Erreur", "Algorithme de hachage invalide.")
        return

    # Vérifier si la longueur du hachage est valide
    if len(hachage_entre) != hash_func().digest_size * 2:
        messagebox.showerror("Erreur", f"Le hachage {algo} doit comporter {hash_func().digest_size * 2} caractères.")
        return

    dictionnaire = charger_dictionnaire("rockyou.txt")
    dictionnaire_hachages = set(hash_func(mot_de_passe.encode('utf-8')).hexdigest() for mot_de_passe in dictionnaire)

    if hachage_entre in dictionnaire_hachages:
        mot_de_passe_trouve = next(mot_de_passe for mot_de_passe in dictionnaire if hash_func(mot_de_passe.encode('utf-8')).hexdigest() == hachage_entre)
        messagebox.showinfo("Mot de passe trouvé", f"Le mot de passe est : {mot_de_passe_trouve}\nLe hachage est : {hachage_entre}")
    else:
        messagebox.showinfo("Mot de passe non trouvé", "Aucun mot de passe correspondant n'a été trouvé dans le dictionnaire.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Recherche de mot de passe")

# Cadre principal
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Étiquette et champ de saisie pour le hachage
hash_label = tk.Label(frame, text="Hachage:")
hash_label.grid(row=0, column=0, sticky="w")

hash_entry = tk.Entry(frame)
hash_entry.grid(row=0, column=1, padx=10)

# Menu déroulant pour sélectionner l'algorithme de hachage
algo_label = tk.Label(frame, text="Algorithme:")
algo_label.grid(row=1, column=0, sticky="w")

algo_var = tk.StringVar()
algo_var.set("MD5")  # Valeur par défaut

algo_options = ["MD5", "SHA-1", "SHA-256", "SHA-3"]
algo_menu = tk.OptionMenu(frame, algo_var, *algo_options)
algo_menu.grid(row=1, column=1, padx=10)

# Bouton pour rechercher le mot de passe
search_button = tk.Button(frame, text="Rechercher", command=lambda: rechercher_mot_de_passe(algo_var.get()))
search_button.grid(row=2, columnspan=2, pady=10)

# Exécution de la boucle principale
root.mainloop()
