import tkinter as tk
from view.register_view_parts import RegisterViewParts


class RegisterView:

    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0)

        self.image1 = RegisterViewParts(self.frame, row=0, col=0)
        self.image2 = RegisterViewParts(self.frame, row=1, col=0)
        self.image3 = RegisterViewParts(self.frame, row=2, col=0)

        self.execute_button = tk.Button(master, text='実行')
        self.execute_button.grid(row=1, column=0)
