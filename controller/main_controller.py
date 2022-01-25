from logger import Logger
from model.main_model import MainModel
from view.main_view import MainView

from controller.register_controller import RegisterController


class MainController:

    def __init__(self, master, config_path):
        self.logger = Logger()
        self.model = MainModel(self.logger, config_path)
        self.view = MainView(master)

        self.register_controller = RegisterController()