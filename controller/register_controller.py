import os
import tkinter as tk
from tkinter import filedialog


def changeText(label):
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

    label.set(path)

    # if path != '':
    #     entry.delete(0, tk.END)
    #     entry.insert(0, path)


class RegisterController:

    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.image1.image_path.config(textvariable=self.model.register_model.image_path1)
        self.view.image1.image_button.config(command=lambda: changeText(self.model.register_model.image_path1))

        self.view.image2.image_path.config(textvariable=self.model.register_model.image_path2)
        self.view.image2.image_button.config(command=lambda: changeText(self.model.register_model.image_path2))

        self.view.image3.image_path.config(textvariable=self.model.register_model.image_path3)
        self.view.image3.image_button.config(command=lambda: changeText(self.model.register_model.image_path3))
