import hashlib
import random
import tkinter as tk
from tkinter import ttk
import threading
import pickle
import os
import time

def rainbow_attackmd5(hash_value, filename):
    with open(filename, 'r') as f:
        table = [line.strip().split(':') for line in f.readlines()]
    start_time = time.time()
    for hash_end, password_end in table:
        steps_text.insert(tk.END, f"Comparing hash value {hash_value} with hash end {hash_end} and password end {password_end}\n")
        if hash_value == hash_end:
            hash_value = hashlib.md5(password_end.encode()).hexdigest()
            for hash_start, password_start in table:
                steps_text.insert(tk.END, f"Comparing hash value {hash_value} with hash start {hash_start} and password start {password_start}\n")
                if hash_start == hash_value:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    steps_text.insert(tk.END, f"Password found in {elapsed_time:.4f} seconds\n")
                    return password_start
    return None

def rainbow_attacksha1(hash_value, filename):
    with open(filename, 'r') as f:
        table = [line.strip().split(':') for line in f.readlines()]
    start_time = time.time()
    for hash_end, password_end in table:
        steps_text.insert(tk.END, f"Comparing hash value {hash_value} with hash end {hash_end} and password end {password_end}\n")
        if hash_value == hash_end:
            hash_value = hashlib.sha1(password_end.encode()).hexdigest()
            for hash_start, password_start in table:
                steps_text.insert(tk.END, f"Comparing hash value {hash_value} with hash start {hash_start} and password start {password_start}\n")
                if hash_start == hash_value:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    steps_text.insert(tk.END, f"Password found in {elapsed_time:.4f} seconds\n")
                    return password_start
    return None

def search_password(hash_value, hash_type):
    start_time = time.time()
    if hash_type == "MD5":
        password = rainbow_attackmd5(hash_value, "table.txt")
    elif hash_type == "SHA1":
        password = rainbow_attacksha1(hash_value, "tablesha1.txt")
    end_time = time.time()
    elapsed_time = end_time - start_time

    if password:
        password_label.config(text=f'The original password was: {password}')
        time_label.config(text=f'Password found in {elapsed_time:.4f} seconds')
    else:
        password_label.config(text='The password could not be found in the rainbow table.')
        time_label.config(text='')

root = tk.Tk()
root.title("Rainbow Table Attack")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

hash_label = ttk.Label(frame, text="Enter hash value:")
hash_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))

hash_entry = ttk.Entry(frame, width=35)
hash_entry.grid(row=0, column=1, sticky=tk.E)

hash_type_label = ttk.Label(frame, text="Select hash type:")
hash_type_label.grid(row=1, column=0, sticky=tk.W, padx=(0, 10))

hash_type = tk.StringVar()
hash_type.set("MD5")
hash_type_menu = ttk.OptionMenu(frame, hash_type, "MD5", "SHA1")
hash_type_menu.grid(row=1, column=1, sticky=tk.E)

search_button = ttk.Button(frame, text="Search", command=lambda: search_password(hash_entry.get(), hash_type.get()))
search_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

password_label = ttk.Label(frame, text="")
password_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

time_label = ttk.Label(frame, text="")
time_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

steps_text = tk.Text(frame, height=10, width=50)
steps_text.grid(row=5, column=0, columnspan=2, pady=(10, 0))

root.mainloop()
