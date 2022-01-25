import tkinter as tk


class RegisterView:

    def __init__(self, master):
        self.execute_button = tk.Button(master, text='実行')
        self.execute_button.grid(row=0, column=0)