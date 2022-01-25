import tkinter as tk
from controller.main_controller import MainController


def main():
    root = tk.Tk()
    app = MainController(master=root, config_path='config.ini')  # Inherit
    root.mainloop()


if __name__ == "__main__":
    main()
