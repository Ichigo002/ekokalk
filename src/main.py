from .main_window import EkokalkWindow


if __name__ == "__main__":
    win = EkokalkWindow("Solar panel calculator", "400x460")
    win.create_widgets()
    win.run()