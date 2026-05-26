import json
from pathlib import Path

from rich.console import Console
from rich.theme import Theme

import settings


class ScreenAdapter():
    def __init__(self):
        self.references = self.get_reference_json()

    def get_reference_json(self) -> dict:
        file_path = Path(__file__).parent / f"utils/{settings.DISPLAY_TYPE}_references.json"

        with open(file_path, "r") as data:
            data = json.load(data)
            return data

    def return_menu(self, menu_list: list) -> list:
        visible_menu = []

        for i in range(0, len(menu_list)):
            visible_menu.append(f"{i}. {menu_list[i]}")

        return "\n".join(visible_menu)

    def prepare_text_for_formatting(self, text_item: str|list) -> str:
        result = text_item

        if isinstance(text_item, list):
            result = self.return_menu(text_item)

        elif isinstance(text_item, str):
            for key, value in self.references.items():
                result = result.replace(key, value)
        
        return result

    def print_console(self, type_text: str, text_content: str):
        custom_theme = Theme({
            "welcome_title": "bold dim yellow",
            "explanation": "italic cyan",
        })

        console = Console(theme=custom_theme)
        if type_text == "title":
            print("\n")
            console.rule(text_content, style="dim cyan")
            print("\n")

        if type_text == "explanation":
            console.print(text_content, justify="center")

        if type_text == "menu":
            console.print(text_content)

    def print_texts(self, texts: dict):
        all_keys = self.references.keys()

        for key, value in texts.items():
            value = self.prepare_text_for_formatting(value)
            
            if settings.DISPLAY_TYPE == "console":
                self.print_console(key, value)


class Screen():
    def __init__(self, page_name):
        self.adapter = ScreenAdapter()
        self.texts = self.fetch_json(page_name)

    def fetch_json(self, page_name: str) -> dict:
        file_path = Path(__file__).parent / "utils/page_texts.json"

        with open(file_path, "r") as data:
            data = json.load(data)
            return data[page_name]

    def display_screen(self):
        self.adapter.print_texts(self.texts)

class MainScreen(Screen):
    def __init__(self):
        super().__init__("main")


class WelcomeScreen(Screen):
    def __init__(self):
        super().__init__("welcome")
