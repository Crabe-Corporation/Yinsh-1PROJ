"""
CLASSES UI
Gestion de l'interface graphique du jeu et du menu principal
"""

from tkinter import *
from pawn import YinshPawn
from board import X_OFFSETS, H
DEFAULT_FONT = ("Helvetica", 16)
GRID_OFFSET = (50, 61)

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

        self.__color_scheme = {
            "pawns": (
                "#C55A11", "blue"
            )
        }

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

        from pawn import YinshPawn
        self.draw_pawn(1, 3, YinshPawn(0, "pawn"))
        self.draw_pawn(1, 2, YinshPawn(1, "marking"))
        self.draw_pawn(1, 1, YinshPawn(1, "pawn"))
        self.draw_pawn(9, 10, YinshPawn(0, "marking"))
        self.draw_pawn(6, 10, YinshPawn(1, "marking"))

        self.__root.mainloop()

    def draw_board(self) -> None:
        image_file = PhotoImage(file="grid.png")
        self.__canvas.create_image(GRID_OFFSET[0], GRID_OFFSET[1], image=image_file, anchor=NW)
        self.__canvas.image = image_file

    def draw_pawn(self, x: int, y: int, pawn: YinshPawn) -> int:
        if pawn.get_pawn_type() == "marking":
            return self.__canvas.create_oval(X_OFFSETS[x] + y * 66.5 - 20 + GRID_OFFSET[0],
                                              H * x - 20 + GRID_OFFSET[1],
                                              X_OFFSETS[x] + y * 66.5 + 20 + GRID_OFFSET[0],
                                              H * x + 20 + GRID_OFFSET[1],
                                              fill=self.__color_scheme["pawns"][pawn.get_player()], width=0)
        else:
            return self.__canvas.create_oval(X_OFFSETS[x] + y * 66.5 - 25 + GRID_OFFSET[0],
                                              H * x - 25 + GRID_OFFSET[1],
                                              X_OFFSETS[x] + y * 66.5 + 25 + GRID_OFFSET[0],
                                              H * x + 25 + GRID_OFFSET[1],
                                              fill="", outline=self.__color_scheme["pawns"][pawn.get_player()], width=8)


class YinshMenu():
    def __init__(self) -> None:
        pass