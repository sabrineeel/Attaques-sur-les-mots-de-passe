import hashlib
import string
import random

def reduce_hash(hashed_value):
    """Reduces the length of the hashed value by taking the first 8 characters."""
    return hashed_value[:12]

def hash_word(word):
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    return hashed_word

def generate_random_word(length=12):
    """Generates a random word of the given length using lowercase and uppercase letters and digits."""
    letters = string.ascii_letters + string.digits
    random_word = ''.join(random.choice(letters) for i in range(length))
    return random_word
def create_rainbow_table(nbr_mots, num_iterations):
    table = {}
    for i in range(nbr_mots):
        random_word = generate_random_word()
        #print("This is the random word :"+random_word)
        hashed_word = hash_word(random_word)
        reduced_hash = reduce_hash(hashed_word)
       
        for _ in range(num_iterations):
            hashed_word = hash_word(reduced_hash)
            #print("This is the hash :"+hashed_word)
            reduced_hash2 = reduce_hash(hashed_word)           
            #print("This is the reduced hash:"+reduced_hash2+"\n")
            reduced_hash = reduced_hash2
        table[i] = random_word,reduced_hash2
    return table

def save_table_to_file(table, filename):
    """Saves the rainbow table to a file."""
    with open(filename, 'w') as f:
        for word, hash_value in table.values():
            f.write(f"{word},{hash_value}\n")

if __name__ == "__main__":
    nbr_mots=1000
    num_iterations = 100
    table = create_rainbow_table(nbr_mots,num_iterations)
    filename = "rainbow_table(12_caracteres).txt"
    save_table_to_file(table, filename)
 
    


