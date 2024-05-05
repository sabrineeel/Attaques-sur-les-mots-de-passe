import hashlib
import os
import time
import time
import tkinter as tk
from tkinter import messagebox
#LES FONCTIONS DE REDUCTION
def reduce_hash_6_caracters(hashed_value):
    return hashed_value[:6]
def reduce_hash_7_caracters(hashed_value):
    return hashed_value[:7]
def reduce_hash_8_caracters(hashed_value):
    return hashed_value[:8]
def reduce_hash_9_caracters(hashed_value):
    return hashed_value[:9]
def reduce_hash_10_caracters(hashed_value):
    return hashed_value[:10]
def reduce_hash_11_caracters(hashed_value):
    return hashed_value[:11]
def reduce_hash_12_caracters(hashed_value):
    return hashed_value[:12]


def hash_word(word):
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    return hashed_word

def load_rainbow_table(filename):
    """Loads the rainbow table from a file."""
    table = {}
    with open(filename, 'r') as f:
        for line in f:
            word, hash_value = line.strip().split(',')
            table[hash_value] = word
    return table

def search_rainbow_table(hash_value, table):
    """Searches for a hash in the rainbow table."""
    if hash_value in table:
        return table[hash_value]
    return None
def crack_password_6caracters(hash_value, table):
    password = search_rainbow_table(hash_value, table)
    if password:
        print(password)
        for j in range(1000):
            word = hash_word(password)
           # print(word)
            password = reduce_hash_6_caracters(word)
           # print(password)
        return password
    else:
        for word, hash_value_table in table.items():
            #print(hash_value_table)
            hashed_word = hash_word(hash_value_table)
            #print(hashed_word)
            hashreduit = reduce_hash_6_caracters(hashed_word)           
            if hashreduit == hash_value:
                return hash_value_table  # <--- Return immediately when match found
            for k in range(1000):     
                                       
                reduced_hash = reduce_hash_6_caracters(hashed_word)
              #  print(reduced_hash)
                if reduced_hash == hash_value:                  
                    return motdepasse  # <--- Return immediately when match found
               
                hashed_word = hash_word(reduced_hash)
                motdepasse=reduced_hash
               # print(hashed_word)
                
        return None
def crack_password_7caracters(hash_value, table):
    password = search_rainbow_table(hash_value, table)
    if password:
        print(password)
        for j in range(1000):
            word = hash_word(password)
          
            password = reduce_hash_7_caracters(word)
          
        return password
    else:
        for word, hash_value_table in table.items():
           
            hashed_word = hash_word(hash_value_table)
            
            hashreduit = reduce_hash_7_caracters(hashed_word)           
            if hashreduit == hash_value:
                return hash_value_table 
            for k in range(1000):     
                                       
                reduced_hash = reduce_hash_7_caracters(hashed_word)
                
                if reduced_hash == hash_value:                  
                    return motdepasse  
               
                hashed_word = hash_word(reduced_hash)
                motdepasse=reduced_hash
                
                
        return None

def crack_password_8caracters(hash_value, table):
    password = search_rainbow_table(hash_value, table)
    if password:
        print(password)
        for j in range(1000):
            word = hash_word(password)
           
            password = reduce_hash_8_caracters(word)
           
        return password
    else:
        for word, hash_value_table in table.items():
            
            hashed_word = hash_word(hash_value_table)
            
            hashreduit = reduce_hash_8_caracters(hashed_word)           
            if hashreduit == hash_value:
                return hash_value_table  
            for k in range(1000):     
                                       
                reduced_hash = reduce_hash_8_caracters(hashed_word)
                
                if reduced_hash == hash_value:                  
                    return motdepasse  
               
                hashed_word = hash_word(reduced_hash)
                motdepasse=reduced_hash
              
                
        return None
    
def crack_password_9caracters(hash_value, table):
    password = search_rainbow_table(hash_value, table)
    if password:
        print(password)
        for j in range(1000):
            word = hash_word(password)
           
            password = reduce_hash_9_caracters(word)
           
        return password
    else:
        for word, hash_value_table in table.items():
          
            hashed_word = hash_word(hash_value_table)
            
            hashreduit = reduce_hash_9_caracters(hashed_word)           
            if hashreduit == hash_value:
                return hash_value_table 
            for k in range(1000):     
                                       
                reduced_hash = reduce_hash_9_caracters(hashed_word)
              
                if reduced_hash == hash_value:                  
                    return motdepasse  
               
                hashed_word = hash_word(reduced_hash)
                motdepasse=reduced_hash
                
                
        return None
        
def crack_password_10caracters(hash_value, table):
    password = search_rainbow_table(hash_value, table)
    if password:
        print(password)
        for j in range(1000):
            word = hash_word(password)
           
            password = reduce_hash_10_caracters(word)
           
        return password
    else:
        for word, hash_value_table in table.items():
            
            hashed_word = hash_word(hash_value_table)
           
            hashreduit = reduce_hash_10_caracters(hashed_word)           
            if hashreduit == hash_value:
                return hash_value_table  
            for k in range(1000):     
                                       
                reduced_hash = reduce_hash_10_caracters(hashed_word)
             
                if reduced_hash == hash_value:                  
                    return motdepasse  
               
                hashed_word = hash_word(reduced_hash)
                motdepasse=reduced_hash
               
                
        return None
    
def crack_password_11caracters(hash_value, table):
    password = search_rainbow_table(hash_value, table)
    if password:
        print(password)
        for j in range(1000):
            word = hash_word(password)
           
            password = reduce_hash_11_caracters(word)
          
        return password
    else:
        for word, hash_value_table in table.items():
            
            hashed_word = hash_word(hash_value_table)
            
            hashreduit = reduce_hash_11_caracters(hashed_word)           
            if hashreduit == hash_value:
                return hash_value_table  
            for k in range(1000):     
                                       
                reduced_hash = reduce_hash_11_caracters(hashed_word)
             
                if reduced_hash == hash_value:                  
                    return motdepasse  
               
                hashed_word = hash_word(reduced_hash)
                motdepasse=reduced_hash
               
                
        return None
def crack_password_12caracters(hash_value, table):
    password = search_rainbow_table(hash_value, table)
    if password:
        print(password)
        for j in range(1000):
            word = hash_word(password)           
            password = reduce_hash_12_caracters(word)
           
        return password
    else:
        for word, hash_value_table in table.items():        
            hashed_word = hash_word(hash_value_table)        
            hashreduit = reduce_hash_12_caracters(hashed_word)           
            if hashreduit == hash_value:
                return hash_value_table  
            for k in range(1000):                                           
                reduced_hash = reduce_hash_12_caracters(hashed_word)              
                if reduced_hash == hash_value:                  
                    return motdepasse  
               
                hashed_word = hash_word(reduced_hash)
                motdepasse=reduced_hash
               
                
        return None
        

def main(hash_value, label):
    start_time = time.time()
    filename = "rainbow_table(6_caracteres).txt"
    table = load_rainbow_table(filename)
    reduced_hash_value = reduce_hash_6_caracters(hash_value)
    password = crack_password_6caracters(reduced_hash_value, table)
    if (password == None):
        filename = "rainbow_table(7_caracteres).txt"
        table = load_rainbow_table(filename)
        reduced_hash_value = reduce_hash_7_caracters(hash_value)
        password = crack_password_7caracters(reduced_hash_value, table)
        if (password == None):
            filename = "rainbow_table(8_caracteres).txt"
            table = load_rainbow_table(filename)
            reduced_hash_value = reduce_hash_8_caracters(hash_value)
            password = crack_password_8caracters(reduced_hash_value, table)
            if (password == None):
                filename = "rainbow_table(9_caracteres).txt"
                table = load_rainbow_table(filename)
                reduced_hash_value = reduce_hash_9_caracters(hash_value)
                password = crack_password_9caracters(reduced_hash_value, table)
                if (password == None):
                    filename = "rainbow_table(10_caracteres).txt"
                    table = load_rainbow_table(filename)
                    reduced_hash_value = reduce_hash_10_caracters(hash_value)
                    password = crack_password_10caracters(reduced_hash_value, table)
                    if (password == None):
                        filename = "rainbow_table(11_caracteres).txt"
                        table = load_rainbow_table(filename)
                        reduced_hash_value = reduce_hash_11_caracters(hash_value)
                        password = crack_password_11caracters(reduced_hash_value, table)
                        if (password == None):
                            filename = "rainbow_table(12_caracteres).txt"
                            table = load_rainbow_table(filename)
                            reduced_hash_value = reduce_hash_12_caracters(hash_value)
                            password = crack_password_12caracters(reduced_hash_value, table)

    elapsed_time = time.time() - start_time
    if password:
        label.config(text=f"Password found: {password}\nSearch time: {elapsed_time:.4f} seconds")
    else:
        label.config(text=f"Password not found in rainbow table.\n")

def gui():
    root = tk.Tk()
    root.title("Attaque Arc en ciel")
    tk.Label(root, text="Enter hash value:").pack()
    hash_value = tk.Entry(root, width=50, borderwidth=3)
    hash_value.pack()
    button = tk.Button(root, text="Crack Password", command=lambda: main(hash_value.get(), label))
    button.pack()
    label = tk.Label(root, text="", font=("Arial", 18), fg="black")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    gui()
