import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.configure(bg='#e0ffff')  

        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.headline_label = ttk.Label(self.root, text="Currency Converter", background='#e0ffff', font=('Arial', 16, 'bold'))
        self.headline_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.from_currency_label = ttk.Label(self.root, text="From Currency", background='#e0ffff', font=('Arial', 12))
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.from_currency_option = ttk.Combobox(self.root, textvariable=self.from_currency_var, font=('Arial', 12), width=20, state='readonly')
        self.from_currency_option.grid(row=1, column=1, padx=10, pady=10)

        self.to_currency_label = ttk.Label(self.root, text="To Currency", background='#e0ffff', font=('Arial', 12))
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.to_currency_option = ttk.Combobox(self.root, textvariable=self.to_currency_var, font=('Arial', 12), width=20, state='readonly')
        self.to_currency_option.grid(row=2, column=1, padx=10, pady=10)

        self.amount_label = ttk.Label(self.root, text="Amount", background='#e0ffff', font=('Arial', 12))
        self.amount_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.amount_entry = ttk.Entry(self.root, textvariable=self.amount_var, font=('Arial', 12), width=20)
        self.amount_entry.grid(row=3, column=1, padx=10, pady=10)

        self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert, style='TButton', width=10)
        self.convert_button.grid(row=4, column=1, padx=10, pady=10, sticky='e')

        self.result_label = ttk.Label(self.root, text="Converted Amount:", background='#e0ffff', font=('Arial', 12))
        self.result_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.result_value_label = ttk.Label(self.root, textvariable=self.result_var, background='#e0ffff', font=('Arial', 12, 'bold'), foreground='blue')
        self.result_value_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        self.exit_button = ttk.Button(self.root, text="Exit", command=root.destroy, style='TButton', width=10)
        self.exit_button.grid(row=6, column=1, padx=10, pady=10, sticky='e')

        self.clear_button = ttk.Button(self.root, text="Clear", command=self.clear_fields, style='TButton', width=10)
        self.clear_button.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.fullscreen_button = ttk.Button(self.root, text="Toggle Fullscreen", command=self.toggle_fullscreen, style='TButton', width=15)
        self.fullscreen_button.grid(row=6, column=0, padx=10, pady=10, sticky='w')

        self.footer_label = ttk.Label(self.root, text="Made by: Harsh Bhardwaj", background='#e0ffff', font=('Times New Roman', 10, 'italic'))
        self.footer_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        
        self.populate_currency_options()

    def populate_currency_options(self):
    
        try:
            url = "https://api.exchangerate-api.com/v4/latest/USD"
            response = requests.get(url)
            data = response.json()
            rates = data.get('rates', {})
            currencies = list(rates.keys())
            currencies.insert(0, 'USD')  
            self.from_currency_option['values'] = currencies
            self.to_currency_option['values'] = currencies
            self.from_currency_var.set('USD')
            self.to_currency_var.set('INR') 
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Failed to fetch currency data. Please check your internet connection.")

    def convert(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = self.amount_var.get()

        if not from_currency or not to_currency or not amount:
            messagebox.showerror("Error", "Please enter all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
            return

        try:
            conversion = self.get_currency_rate(from_currency, to_currency)
            if conversion:
                converted_amount = amount * conversion
                self.result_var.set(f"{converted_amount:.2f} {to_currency}")
            else:
                messagebox.showerror("Error", f"Unable to convert from {from_currency} to {to_currency}.")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Failed to fetch currency conversion rate. Please check your internet connection.")

    def get_currency_rate(self, from_currency, to_currency):
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        rates = data.get('rates')
        if rates:
            return rates.get(to_currency)
        else:
            return None

    def clear_fields(self):
        self.from_currency_var.set('')
        self.to_currency_var.set('')
        self.amount_var.set('')
        self.result_var.set('')

    def toggle_fullscreen(self):
        
        if self.root.attributes('-fullscreen'):
            self.root.attributes('-fullscreen', False)
        else:
            self.root.attributes('-fullscreen', True)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x300")
    root.resizable(False, False)
    root.configure(bg='#e0ffff') 

    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12))

    converter = CurrencyConverter(root)
    root.mainloop()
