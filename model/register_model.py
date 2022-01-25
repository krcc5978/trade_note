import tkinter as tk


class RegisterModel:

    def __init__(self):
        self.image_path1 = tk.StringVar()
        self.image_path2 = tk.StringVar()
        self.image_path3 = tk.StringVar()

        self.conbobox_text = tk.StringVar()
        self.conbobox_value = []
