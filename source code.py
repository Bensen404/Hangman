from tkinter import *
import tkinter as tk
from wonderwords import RandomWord 
from tkinter import messagebox  # Import messagebox for showing messages
import random

# random_word = RandomWord()
# word_list = [random_word.word().upper()]

photos = []  

def load_images():
    global photos
    for i in range(12):  
        image = PhotoImage(file=f"images/hang{i}.png")
        photos.append(image)

def start_new_game():
    global the_word_withSpaces
    global numberOfGuesses
    global lblWord
    global guessed 
    global imgLabel # To store the guessed letters
    title_label.destroy()
    new_gbutton.destroy()

    random_word = RandomWord()
    word_list = [random_word.word().upper()]

    create_keyboard()

    imgLabel = tk.Label(root,bg='#FFFFFF')
    imgLabel.pack(pady=20)

    numberOfGuesses = 0
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)  
    lblWord_text = ["_"] * len(the_word)  
    lblWord.set(" ".join(lblWord_text))  
    imgLabel.config(image=photos[0],height=300, width=300) 
    guessed = lblWord_text  # Initialize guessed letters

def restart():
    global imgLabel
    global keyboard_frame
    global lblWord
    global word_label

    imgLabel.destroy()
    keyboard_frame.destroy()
    start_new_game()

def letter_click(letter):
    global numberOfGuesses
    global guessed
    global imgLabel  # Use the global guessed list

    if numberOfGuesses < 11:    
        txt = list(the_word_withSpaces.replace(" ", ""))  # List of characters in the word without spaces
        
        if letter in txt:  # Check if the letter is in the word
            for c in range(len(txt)):
                if txt[c] == letter: 
                    guessed[c] = letter  
            lblWord.set(" ".join(guessed))  # Update the label with the new guessed word
            
            if "_" not in guessed:  # Check if the word is completely guessed
                response=messagebox.askyesno("Hangman", "You guessed it!\n Wanna Continue?")  # Show success message
                if response==1:
                    restart()
                else:
                    root.destroy()
        else:
            numberOfGuesses += 1  # Increment guesses if the letter is wrong
            imgLabel.config(image=photos[numberOfGuesses])  # Change the hangman image  # Change the hangman image
            if numberOfGuesses==11:
                response=messagebox.askyesno("Hangman","Game Over\n Wanna Continue?")
                if response==1:
                    restart()
                else:
                    root.destroy()

def create_keyboard():
    global keyboard_frame
    # Create a frame for the on-screen keyboard
    keyboard_frame = tk.Frame(root, bg='#011f46')
    keyboard_frame.pack(expand=True)
    keyboard_frame.place(relx=0.5, rely=1.0, anchor=tk.S)
    
    # QWERTY keyboard layout
    qwerty_layout = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]

    # Create buttons for each letter in QWERTY layout
    r = 0
    for row in qwerty_layout:
        c = 0
        for letter in row:
            # Use a default argument in lambda to capture the current letter
            button = tk.Button(keyboard_frame, text=letter, font=("Helvetica", 18), width=4, height=2, command=lambda l=letter: letter_click(l))
            button.grid(row=r, column=c, padx=5, pady=5)
            c += 1
        r += 1

# Create the main window
root = tk.Tk()
root.title("Hangman")
root.geometry("1920x1080")
root.configure(bg='#011f46')

# Load images after creating the main window
load_images()

# Create a label to show the word
lblWord = StringVar()
word_label = tk.Label(root, textvariable=lblWord, font=("Helvetica", 36), bg='#011f46', fg='white')
word_label.pack(pady=20)
center_frame = tk.Frame(root, bg='#011f46')
center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title_label = tk.Label(center_frame, text="Hangman", font=("Helvetica", 48), bg='#011f46', fg='white')
title_label.pack(pady=50)

new_gbutton = tk.Button(center_frame, text="New Game", font=("Helvetica", 24), command=start_new_game)
new_gbutton.pack(pady=20)

'''imgLabel = tk.Label(root,bg='#FFFFFF')
imgLabel.pack(pady=20)'''

root.mainloop()