from .main_window import EkokalkWindow


if __name__ == "__main__":
    win = EkokalkWindow("Solar panel calculator", "400x760")
    win.create_widgets()
    win.run()