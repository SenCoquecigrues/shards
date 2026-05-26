import json
from pathlib import Path

class MenuHandler:
    def __init__(self):
        self.menus = self.fetch_json()

    def fetch_json(self):
        file_path = Path(__file__).parent / "utils/menus.json"

        with open(file_path, "r") as menu_file:
            return json.load(menu_file)

    def return_menu(self, menu_name):
        menu = self.menus[menu_name]
        visible_menu = []

        for i in range(0, len(menu)):
            visible_menu.append(f"{i}. {menu[i]}")

        return visible_menu