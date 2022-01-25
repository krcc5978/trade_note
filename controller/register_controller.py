import os
import cv2
import ast
import tkinter as tk
from tkinter import filedialog


def changeText(label, file_type='*'):
    fTyp = [("", file_type)]
    iDir = os.path.abspath(os.path.dirname(__file__))
    path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

    label.set(path)


def click_word(event, path):
    if not os.path.exists(path):
        return
    img = cv2.imread(path)
    resize_img = cv2.resize(img, dsize=(640, 380))
    cv2.imshow('image', resize_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class RegisterController:

    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.image1.image_path.config(textvariable=self.model.register_model.image_path1)
        self.view.image1.image_button.config(command=lambda: changeText(self.model.register_model.image_path1,
                                                                        '*.png;*.jpg'))
        self.view.image1.image_path.bind("<Button-1>",
                                         lambda event: click_word(event, self.model.register_model.image_path1.get())
                                         )

        self.view.image2.image_path.config(textvariable=self.model.register_model.image_path2)
        self.view.image2.image_button.config(command=lambda: changeText(self.model.register_model.image_path2,
                                                                        '*.png;*.jpg'))
        self.view.image2.image_path.bind("<Button-1>",
                                         lambda event: click_word(event, self.model.register_model.image_path1.get())
                                         )

        self.view.image3.image_path.config(textvariable=self.model.register_model.image_path3)
        self.view.image3.image_button.config(command=lambda: changeText(self.model.register_model.image_path3,
                                                                        '*.png;*.jpg'))
        self.view.image3.image_path.bind("<Button-1>",
                                         lambda event: click_word(event, self.model.register_model.image_path1.get())
                                         )

        output_dir_tuple = ast.literal_eval(self.model.config['widjet']['currency_pair'])
        self.view.pair_combobox.config(textvariable=self.model.register_model.conbobox_text,
                                       values=output_dir_tuple)
