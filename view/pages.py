import json
from pathlib import Path

from view.menu_handler import MenuHandler

class Page():
    def __init__(self, page_name):
        menu_handler = MenuHandler()
        self.menu = menu_handler.return_menu(page_name)
        self.text = self.fetch_json(page_name)

    def fetch_json(self, page_name):
        file_path = Path(__file__).parent / "utils/page_texts.json"

        with open(file_path, "r") as data:
            data = json.load(data)
            return data[page_name]

    def display_page(self):
        print(self.text)

        for entry in self.menu:
            print(entry)


class MainPage(Page):
    def __init__(self):
        super().__init__("main")


class WelcomePage(Page):
    def __init__(self):
        super().__init__("welcome")