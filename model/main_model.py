import sqlite3


class MainModel:

    def __init__(self, logger, config_path):
        self.logger = logger
        self.conn = sqlite3.connect('trade_note.db')
