"""
CLASSES UI
Gestion de l'interface graphique du jeu et du menu principal
"""

from tkinter import *
from pawn import YinshPawn
DEFAULT_FONT = ("Helvetica", 16)

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

        logo_file = PhotoImage(file="logo.png")
        Label(self.__scoreboard, image=logo_file).pack()
        text_gamemode = "Blitz" if settings[0] else "Normal"
        text_gamemode += ", en réseau" if settings[1] else ", local"
        pawns_to_win = 1 if settings[0] else 5
        Label(self.__scoreboard, text=f"Mode de jeu: {text_gamemode}", font=DEFAULT_FONT, padx=10, pady=30).pack()
        self.__player_texts = [
            StringVar(value=f"Joueur 1: 0/{pawns_to_win} pions"),
            StringVar(value=f"Joueur 2: 0/{pawns_to_win} pions")
        ]
        self.__player_labels = [
            Label(self.__scoreboard, textvariable=self.__player_texts[0], font=DEFAULT_FONT, padx=10).pack(),
            Label(self.__scoreboard, textvariable=self.__player_texts[1], font=DEFAULT_FONT, padx=10).pack()
        ]

        self.draw_board()

        self.__root.mainloop()

    def draw_board(self) -> None:
        image_file = PhotoImage(file="grid.png")
        self.__canvas.create_image(50, 61, image=image_file, anchor=NW)
        self.__canvas.image = image_file

    def draw_pawn(self, x: int, y: int, pawn: YinshPawn) -> tuple:
        pass


class YinshMenu():
    def __init__(self) -> None:
        pass