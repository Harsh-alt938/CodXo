import tkinter as tk
from tkinter import ttk, messagebox
import random
import pygame

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.configure(bg='#ffebcd')  # Set background color
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.player_name = ""
        self.full_screen = False

        # Initialize pygame mixer for sound effects
        pygame.mixer.init()

        self.title_label = ttk.Label(self.root, text="Number Guessing Game", background='#ffebcd', font=('Arial', 16, 'bold'))
        self.title_label.pack(pady=10)

        self.name_label = ttk.Label(self.root, text="Enter your name:", background='#ffebcd', font=('Arial', 12))
        self.name_label.pack(pady=5)

        self.name_entry = ttk.Entry(self.root, font=('Arial', 12))
        self.name_entry.pack(pady=5)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_game, style='TButton', width=10)
        self.start_button.pack(pady=5)

        self.instruction_label = ttk.Label(self.root, text="", background='#ffebcd', font=('Arial', 12))
        self.instruction_label.pack(pady=5)

        self.guess_entry = ttk.Entry(self.root, font=('Arial', 12))
        self.guess_entry.pack(pady=5)
        self.guess_entry.pack_forget()

        self.guess_button = ttk.Button(self.root, text="Guess", command=self.check_guess, style='TButton', width=10)
        self.guess_button.pack(pady=5)
        self.guess_button.pack_forget()

        self.result_label = ttk.Label(self.root, text="", background='#ffebcd', font=('Arial', 12, 'italic'))
        self.result_label.pack(pady=5)

        self.exit_button = ttk.Button(self.root, text="Exit", command=root.destroy, style='TButton', width=20)
        self.exit_button.pack(pady=10)
        self.exit_button.pack_forget()

        self.full_screen_button = ttk.Button(self.root, text="Toggle Full Screen", command=self.toggle_full_screen, style='TButton', width=20)
        self.full_screen_button.pack(pady=10)
        self.full_screen_button.pack_forget()

        self.footer_label = ttk.Label(self.root, text="Made by: Harsh Bhardwaj", background='#ffebcd', font=('Times New Roman', 10, 'italic'))
        self.footer_label.pack(side='bottom', pady=5)

    def start_game(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showerror("Invalid Input", "Please enter your name.")
            return

        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        self.name_label.config(text=f"Welcome, {self.player_name}!")
        self.instruction_label.config(text="Guess a number between 1 and 100")
        self.guess_entry.pack(pady=5)
        self.guess_button.pack(pady=5)
        self.exit_button.pack(pady=5)
        self.full_screen_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        self.attempts += 1

        # Play input number audio
        pygame.mixer.music.load('input_sound.mp3')
        pygame.mixer.music.play()

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.", foreground='blue')
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.", foreground='blue')
        else:
            self.result_label.config(text=f"Congratulations, {self.player_name}! You've guessed the number in {self.attempts} attempts.", foreground='green')
            # Play winning audio
            pygame.mixer.music.load('winning_sound.mp3')
            pygame.mixer.music.play()
            self.reset_game()

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def toggle_full_screen(self):
        self.full_screen = not self.full_screen
        self.root.attributes("-fullscreen", self.full_screen)

if __name__ == "__main__":
    root = tk.Tk()

    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12))

    game = NumberGuessingGame(root)
    root.mainloop()
