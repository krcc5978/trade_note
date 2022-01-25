import tkinter as tk
import tkinter.ttk as ttk
from view.register_view_parts import RegisterViewParts


class RegisterView:

    def __init__(self, master):
        # self.frame = tk.Frame(master)
        # self.frame.grid(row=0, column=0)

        self.image1 = RegisterViewParts(master, row=0, col=0)
        self.image2 = RegisterViewParts(master, row=1, col=0)
        self.image3 = RegisterViewParts(master, row=2, col=0)

        self.pair = tk.Label(master, text='通貨ペア')
        self.pair.grid(row=4, column=0, padx=(10, 0), pady=(10, 0), sticky=tk.W)

        self.pair_combobox = ttk.Combobox(master, state="readonly")
        self.pair_combobox.grid(row=4, column=1, padx=(10, 0), pady=(10, 0), sticky=tk.W)

        self.execute_button = tk.Button(master, text='実行')
        self.execute_button.grid(row=5, column=1, padx=(10, 0), pady=(10, 0), sticky=tk.W)
