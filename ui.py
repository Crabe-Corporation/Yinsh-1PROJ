"""
CLASSES UI
Gestion de l'interface graphique du jeu et du menu principal
"""

from tkinter import *
from pawn import YinshPawn
from board import X_OFFSETS, H, find_closest_point
DEFAULT_FONT = ("Helvetica", 16)
GRID_OFFSET = (50, 61)

"""
YinshUI()
- settings (tuple) : paramètres de la partie sous la forme (mode blitz/jeu en réseau). Valeur par défaut = (True, False). Transformé en dictionnaire à l'initialisation.
"""
class YinshUI():
    def __init__(self, game, gamemode: str, gametype: str, players: list) -> None:
        if gamemode in ["Blitz", "Normal"] and gametype in ["Online", "Offline", "Solo"]:
            self.__game_settings = {
                "mode": gamemode,
                "type": gametype
            }
        else:
            raise ValueError("gamemode et/ou gametype invalide(s) !")
        self.__root = Tk()
        self.__root.title("Yinsh")
        self.__root.resizable(False, False)
        self.__game = game

        self.__color_scheme = {
            "pawns": (
                "#C55A11", "blue"
            )
        }

        self.__canvas = Canvas(self.__root, width=700, height=700)
        self.__canvas.bind("<Button-1>", self.__handle_click)
        self.__scoreboard = Frame(self.__root, width=250, height=700)
        self.__canvas.pack(side="left")
        self.__scoreboard.pack(side="left")

        logo_file = PhotoImage(file="logo.png")
        logo_label = Label(self.__scoreboard, image=logo_file)
        logo_label.image = logo_file
        logo_label.pack()
        text_gamemode = self.__game_settings["mode"]
        text_gamemode += ", en réseau" if self.__game_settings["type"] == "Online" else ", local"
        pawns_to_win = 1 if self.__game_settings["mode"] == "Blitz" else 3
        Label(self.__scoreboard, text=f"Mode de jeu: {text_gamemode}", font=DEFAULT_FONT, padx=10, pady=30).pack()
        self.__player_texts = [
            StringVar(value=f"Joueur 1: 0/{pawns_to_win} pions"),
            StringVar(value=f"Joueur 2: 0/{pawns_to_win} pions")
        ]
        self.__player_labels = [
            Label(self.__scoreboard, textvariable=self.__player_texts[0], font=DEFAULT_FONT, padx=10).pack(),
            Label(self.__scoreboard, textvariable=self.__player_texts[1], font=DEFAULT_FONT, padx=10).pack()
        ]

        self.__drawn_shapes = {}

        self.draw_board()

    def run(self):
        self.__root.mainloop()

    def draw_board(self) -> None:
        image_file = PhotoImage(file="grid.png")
        self.__canvas.create_image(GRID_OFFSET[0], GRID_OFFSET[1], image=image_file, anchor=NW)
        self.__canvas.image = image_file

    def draw_pawn(self, x: int, y: int, pawn: YinshPawn) -> int:
        if pawn.get_pawn_type() == "marking":
            shape = self.__canvas.create_oval(X_OFFSETS[x] + y * 66.5 - 20 + GRID_OFFSET[0],
                                              H * x - 20 + GRID_OFFSET[1],
                                              X_OFFSETS[x] + y * 66.5 + 20 + GRID_OFFSET[0],
                                              H * x + 20 + GRID_OFFSET[1],
                                              fill=self.__color_scheme["pawns"][pawn.get_player()], width=0)
        else:
            shape = self.__canvas.create_oval(X_OFFSETS[x] + y * 66.5 - 25 + GRID_OFFSET[0],
                                              H * x - 25 + GRID_OFFSET[1],
                                              X_OFFSETS[x] + y * 66.5 + 25 + GRID_OFFSET[0],
                                              H * x + 25 + GRID_OFFSET[1],
                                              fill="", outline=self.__color_scheme["pawns"][pawn.get_player()], width=8)
        self.__drawn_shapes[f"{x};{y}"] = shape
        return shape

    def __handle_click(self, event: Event) -> None:
        # Envoyer les informations dans la partie logique du jeu
        coordinates = find_closest_point(event.x, event.y)
        self.__game.handle_click(coordinates[0], coordinates[1])

    def erase_pawn(self, x: int, y: int) -> bool:
        if f"{x};{y}" not in self.__drawn_shapes.keys():
            return False
        self.__canvas.delete(self.__drawn_shapes[f"{x};{y}"])
        return True
    
    def set_color(self, x: int, y: int, player: int) -> bool:
        if not f"{x};{y}" in self.__drawn_shapes.keys():
            return False
        self.__canvas.itemconfig(self.__drawn_shapes[f"{x};{y}"], fill=self.__color_scheme["pawns"][player])
        return True

class YinshMenu():
    def __init__(self) -> None:
        self.__game_settings=None
        self.__root=Tk()
        usernames=Frame(self.__root)
        usernames.pack()

        Label(usernames,text="Joueur 1 :", padx=10).pack(side="left")
        self.__nomJoueur1=StringVar()
        self.__nomJoueur1.trace_add("write", self.check_length)
        self.__champJoueur1=Entry(usernames, width=20, textvariable=self.__nomJoueur1)
        self.__champJoueur1.pack(side="left")

        Label(usernames,text="Joueur 2 :", padx=10).pack(side="left")
        self.__nomJoueur2=StringVar()
        self.__nomJoueur2.trace_add("write", self.check_length)
        self.__champJoueur2=Entry(usernames, width=20, textvariable=self.__nomJoueur2)
        self.__champJoueur2.pack(side="left")

        settings=Frame(self.__root, pady=25)
        settings.pack()

        self.__gamemode=StringVar()
        self.__gametype=StringVar()
        self.__gamemode.set("Normal")
        self.__gametype.set("Offline")
        self.__gm_menu=OptionMenu(settings, self.__gamemode, "Normal", "Blitz")
        self.__gm_menu.pack(side="left", padx=10)
        self.__gt_menu=OptionMenu(settings, self.__gametype, "Online", "Offline", "Solo")
        self.__gt_menu.pack(side="left", padx=10)

        Button(self.__root, text="Jouer", command=self.launch).pack()

        self.__root.mainloop()
    
    def check_length(self, var, index, mode):
        nomJoueur = self.__nomJoueur1 if var == "PY_VAR0" else self.__nomJoueur2
        if len(nomJoueur.get())<=15:
            return
        else:
            nomJoueur.set(nomJoueur.get()[0:15])

    def launch(self):
        gamemode=self.__gamemode.get()
        gametype=self.__gametype.get()
        self.__game_settings={"gamemode":gamemode, "gametype":gametype, "players":[self.__nomJoueur1.get(), self.__nomJoueur2.get()]}
        self.__root.destroy()

    def get_settings(self):
        return self.__game_settings