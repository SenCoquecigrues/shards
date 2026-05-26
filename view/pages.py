from view.menu_handler import MenuHandler

class Page():
    def __init__(self, menu_name):
        menu_handler = MenuHandler()
        self.menu = menu_handler.return_menu(menu_name)

    def display_page(self):
        for entry in self.menu:
            print(entry)


class MainPage(Page):
    def __init__(self):
        super().__init__("main_menu")

    def display_page(self):
        print("Velcome")

        super().display_page()


class MainPage(Page):
    def __init__(self):
        super().__init__("welcome_menu")

    def display_page(self):
        print("Velcome")
        
        super().display_page()