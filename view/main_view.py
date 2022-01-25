import tkinter as tk
import tkinter.ttk as ttk

from view.register_view import RegisterView


class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master.geometry("580x320")
        self.master.title('ファイルアップロード')
        self.master.resizable(width=False, height=False)

        # Notebookウィジェットの作成
        self.notebook = ttk.Notebook(self.master)

        # タブの作成
        self.tab_one = tk.Frame(self.notebook)
        self.tab_two = tk.Frame(self.notebook)

        # notebookにタブの追加
        self.notebook.add(self.tab_one, text="登録")
        self.notebook.add(self.tab_two, text="履歴")

        self.register_view = RegisterView(self.tab_one)

        # ウィジェットの配置
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)