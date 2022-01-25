import tkinter as tk


class RegisterViewParts:

    def __init__(self, master, row, col, padx=(10, 0), pady=(10, 0)):
        self.image_label = tk.Label(master, text='画像パス : ')
        self.image_label.grid(row=row, column=col, padx=padx, pady=pady)

        self.image_path = tk.Label(master)
        self.image_path.grid(row=row, column=col + 1, padx=padx, pady=pady)

        self.image_button = tk.Button(master, text='参照')
        self.image_button.grid(row=row, column=col + 2, padx=padx, pady=pady)
