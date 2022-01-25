import sqlite3
from model.register_model import RegisterModel


class MainModel:

    def __init__(self, logger, config_path):
        self.logger = logger
        self.conn = sqlite3.connect('trade_note.db')

        self.register_model = RegisterModel()
