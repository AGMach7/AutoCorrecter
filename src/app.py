import tkinter as tk
from tkinter import messagebox
from spelling_suggestions import get_corrections
from data_preprocessing import *

# load data and calculate probabilities
word_l = process_data('D:/ENSAH/ID/S4/NLP/AutoCorrect/data/shakespeare.txt')
vocab = set(word_l)
word_count_dict = get_count(word_l)
probs = get_probs(word_count_dict)

def on_button_click(event=None):
    try:
        n = int(num_suggestions_box.get())
    except ValueError:
        output_box.config(text="Invalid input for number of suggestions. Please enter a valid integer.")
        return
    
    word = input_box.get()
    if not word.isalpha():
        messagebox.showerror("Invalid Input", "Input must contain only alphabetical characters.")
        # output_box.config(text="Invalid Input. Please enter a word contains contain only alphabetical characters.")
        return
    if not word:
        messagebox.showerror("Invalid Input", "Input must not be empty.")
        # output_box.config(text="Invalid Input. Please enter a none empty word.")
        return
    
    tmp_corrections = get_corrections(word, probs, vocab, n)
    suggestions = ""
    for i, word_prob in enumerate(tmp_corrections):
        st = "Word {}:\t{} ({:.4f})\n".format(i+1, word_prob[0], word_prob[1])
        suggestions += st
    if suggestions:
        output_box.config(text=suggestions, justify="left")
    else:
        output_box.config(text="No suggestions found.")

def confirm_exit():
    if messagebox.askokcancel("Confirm Exit", "Are you sure you want to exit?"):
        root.destroy()

# create the main window
root = tk.Tk()
root.title("Auto-Correction Program")
root.protocol("WM_DELETE_WINDOW", confirm_exit)

# add program description
description = """
This program suggests possible spelling corrections for input words based on a given text corpus.
You can specify how many suggestions you want to see in the 'Number of suggestions' section.
The suggested corrections' probabilities are based on a provided text corpus.
"""
description_label = tk.Label(root, text=description, justify="left", wraplength=600)
description_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# create input label and box
input_label = tk.Label(root, text="Enter a word:")
input_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
input_box = tk.Entry(root)
input_box.grid(row=1, column=1, padx=10, pady=10)

# create num suggestions label and box
num_suggestions_label = tk.Label(root, text="Number of suggestions:")
num_suggestions_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
num_suggestions_box = tk.Entry(root)
num_suggestions_box.insert(0, "5")
num_suggestions_box.grid(row=2, column=1, padx=10, pady=10)

# create output label and box
output_label = tk.Label(root, text="Suggestions will appear here:")
output_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
output_box = tk.Label(root, text="")
output_box.grid(row=3, column=1, padx=10, pady=10)

# create button to initiate correction
button_text = "Correct"
button = tk.Button(root, text=button_text, command=on_button_click)
button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# configure grid layout
root.columnconfigure(1, weight=1)

# bind enter key to button click
root.bind('<Return>', on_button_click)

# start the event loop
root.mainloop()