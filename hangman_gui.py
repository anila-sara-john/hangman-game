from tkinter import *
from tkinter import messagebox
import random
import string
from word_list import word_list  # External file containing list of words
from visuals import visuals_dict  # External file containing hangman visuals per chance lef

def pick_word(word_list):
    # Keep picking a random word until it contains no '-' or spaces
    while True:
        set_word = random.choice(word_list)
        if '-' not in set_word and ' ' not in set_word and set_word != '':
            return set_word.upper()

class HangmanGame:
    def __init__(self, root):

        # Initialize the GUI components and game logic
        self.root = root
        self.root.title("Hangman Game")
        self.root.configure(bg='#111')
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")
        self.alphabet = set(string.ascii_uppercase)  # Set of all ASCII characters in uppercase
        self.set_word = pick_word(word_list)  # Pick a random word form word_list  
        self.set_word_letters = set(self.set_word)  # Set of actual letters in the word
        self.guessed_letters = set()  # Set of letters guessed by the user
        self.chances = 7  # Number of lives
        self.display_word = ['_'] * len(self.set_word)  # List storing the updation of letters in the word
        
        # Main frame for widgets
        self.main_frame = Frame(root, bg='#111', bd=0)
        self.main_frame.pack(expand=True, fill='both', anchor='center', pady=15)

        # Display the welcome message
        self.label_welcome = Label(self.main_frame, text='Welcome to the Hangman Game!\nGuess the word one letter at a time. You have 7 chances. Good luck!', font=('Comic Sans MS', 24), bg='#111', fg='aqua')
        self.label_welcome.pack(pady=15)

        # Display the current status of the word to be guessed
        self.label_display = Label(self.main_frame, text=' '.join(self.display_word), font=('Comic Sans MS', 24, 'bold'), bg='#111', fg='whitesmoke')
        self.label_display.pack(pady=15)
        
        # Input prompt
        self.label_info = Label(self.main_frame, text='Enter a letter:',font=('Comic Sans MS', 24), bg='#111', fg='violet')
        self.label_info.pack()

        # Entry field for user input
        self.label_entry = Entry(self.main_frame, width=4, font=('Arial', 17, 'bold'), bg='lightyellow', fg='darkviolet', justify='center')
        self.label_entry.pack()

        # Guess button
        self.guess_btn = Button(self.main_frame, text='GUESS', font=('Comic Sans MS', 14), bg='plum1', fg='deeppink4', cursor='hand2', command=self.make_guess)
        self.guess_btn.pack(pady=20)

        # Display guessed letters
        self.label_guessed_letters = Label(self.main_frame, text='Your guesses:', font=('Comic Sans MS', 14), bg='#111', fg='aqua')
        self.label_guessed_letters.pack(pady=15)

        self.display_guessed_letters = Label(self.main_frame, text='', font=('Arial', 20), bg='#111', fg='whitesmoke')
        self.display_guessed_letters.pack()

        # Display chances
        self.label_chances = Label(self.main_frame, text=f"Remaining chances: {self.chances}", font=('Comic Sans MS', 14), bg='#111', fg='aqua')
        self.label_chances.pack()

        self.label_error = Label(self.main_frame, text='', font=('Comic Sans MS', 14), bg='#111', fg='red')
        self.label_error.pack(pady=15)

        # Display the Hangman visuals
        self.label_visuals = Label(self.main_frame, text='', font=('Courier', 16, 'bold'), bg='#111', fg='whitesmoke')
        self.label_visuals.pack_forget()

        # Ask if the user needs to quit or restart
        self.restart_btn = Button(self.main_frame, text='RESTART GAME', font=('Comic Sans MS', 14), bg='plum1', fg='deeppink4', cursor='hand2', command=self.restart)
        self.restart_btn.pack()

    def make_guess(self):

        # Initialize user_input and handle the actions followed by clicking the 'GUESS' button
        user_input = self.label_entry.get().upper()
        self.label_entry.delete(0, END)

        # Validate input: must be a single letter in the alphabet
        if len(user_input) != 1 or user_input not in self.alphabet:
            messagebox.showwarning('Invalid character!', 'Please enter a single English letter.')
            return
        
        # Check if the letter was already guessed
        if user_input in self.guessed_letters:
            messagebox.showinfo('Already guessed', 'You already guessed that letter.')
            return

        self.guessed_letters.add(user_input)
        self.display_guessed_letters.config(text=' '.join(sorted(self.guessed_letters)).upper())

        # If the guess is wrong
        if user_input not in self.set_word_letters:
            self.label_error.config(text='Oh! That was a wrong guess.\nTry again.')
            self.chances -= 1
            self.label_chances.config(text=f"Remaining chances: {self.chances}")
            self.label_visuals.config(text=visuals_dict[self.chances], justify='left')
            self.label_visuals.pack()

        # If the guess is right
        else:
            self.label_error.config(text='')
            for index, char in enumerate(self.set_word):
                if char == user_input:
                    self.display_word[index] = user_input
            self.set_word_letters.remove(user_input)
            self.label_display.config(text=' '.join(self.display_word))
            
        # Game Over Conditions
        if not self.set_word_letters:
            messagebox.showinfo("You Won!", f"Congrats! The word was: {self.set_word}")
            self.disable_game()
            
        elif self.chances == 0:
            messagebox.showerror("Game Over", f"You lost! The word was: {self.set_word}")
            self.disable_game()
            
    def restart(self):
        # Destroy all widgets from the current game
        for widget in self.root.winfo_children():
            widget.destroy()
        # Start a new game
        HangmanGame(self.root)

    def disable_game(self):
        # Disable input and buttons after game ends
        self.guess_btn.config(state=DISABLED)
        self.label_entry.config(state=DISABLED)


# Create and start GUI
root = Tk()
game = HangmanGame(root)
root.mainloop()
