"""
CLASSES UI
Gestion de l'interface graphique du jeu et du menu principal
"""

from tkinter import *

"""
YinshUI()
- settings (tuple) : paramètres de la partie sous la forme (mode blitz/jeu en réseau). Valeur par défaut = (True, False). Transformé en dictionnaire à l'initialisation.
"""
class YinshUI():
    def __init__(self, settings = (True, False)) -> None:
        self.__game_settings = {
            "blitz_mode": settings[0],
            "online": settings[1]
        }
        self.__root = Tk()
        self.__root.title("Yinsh")
        self.__root.resizable(False, False)

        self.__canvas = Canvas(self.__root, width=700, height=700)
        self.__scoreboard = Frame(self.__root, width=250, height=700)
        self.__canvas.pack(side="left")
        self.__scoreboard.pack(side="left")

        self.draw_board()

        self.__root.mainloop()

    def draw_board(self) -> None:
        image_file = PhotoImage(file="grid.png")
        self.__canvas.create_image(50, 61, image=image_file, anchor=NW)
        self.__canvas.image = image_file


class YinshMenu():
    def __init__(self) -> None:
        pass