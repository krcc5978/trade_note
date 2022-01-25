import sqlite3
import configparser
from model.register_model import RegisterModel


class MainModel:

    def __init__(self, logger, config_path):
        self.logger = logger
        self.config = configparser.ConfigParser()
        self.config.read(config_path, encoding='UTF-8')
        self.conn = sqlite3.connect('trade_note.db')

        self.register_model = RegisterModel()
