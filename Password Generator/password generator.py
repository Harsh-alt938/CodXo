import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.configure(background="#ADD8E6")

        self.title_label = tk.Label(root, text="Made by: Harsh Bhardwaj", font=("Times New Roman", 16), bg="#ADD8E6")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.length_label = tk.Label(root, text="Password Length:", bg="#ADD8E6")
        self.length_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.grid(row=1, column=1, padx=10, pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="white")
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.password_label = tk.Label(root, text="Generated Password:", bg="#ADD8E6")
        self.password_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.password_display = tk.Label(root, text="", bg="white", relief=tk.SOLID, width=30)
        self.password_display.grid(row=3, column=1, padx=10, pady=5)

    def generate_password(self):
        length = self.length_entry.get()
        if length.isdigit():
            length = int(length)
            if length > 0:
                password = self.generate_random_password(length)
                self.password_display.config(text=password)
            else:
                messagebox.showerror("Error", "Password length must be greater than 0.")
        else:
            messagebox.showerror("Error", "Please enter a valid number for password length.")

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
