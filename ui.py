"""
CLASSES UI
Gestion de l'interface graphique du jeu et du menu principal
"""

from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from pawn import YinshPawn
from board import X_OFFSETS, H, find_closest_point
import tkinter.font as font
DEFAULT_FONT = ("Helvetica", 16)
GRID_OFFSET = (50, 61)

"""
YinshUI()
- settings (tuple) : paramètres de la partie sous la forme (mode blitz/jeu en réseau). Valeur par défaut = (True, False). Transformé en dictionnaire à l'initialisation.
"""
class YinshUI():
    def __init__(self, game, gamemode: str, gametype: str, players: list) -> None:
        if gamemode in ["Blitz", "Normal"] and gametype in ["Offline", "Solo"]:
            self.__game_settings = {
                "mode": gamemode,
                "type": gametype
            }
        else:
            raise ValueError("gamemode et/ou gametype invalide(s) !")
        self.__root = Tk()
        self.__root.iconbitmap("icon.ico")
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
        text_gamemode += ", solo" if self.__game_settings["type"] == "Solo" else ", local"
        self.__pawns_to_win = 1 if self.__game_settings["mode"] == "Blitz" else 3
        Label(self.__scoreboard, text=f"Mode de jeu: {text_gamemode}", font=DEFAULT_FONT, padx=10, pady=30).pack()
        self.__player_names = [
            "Joueur 1" if players[0] == "" else players[0],
            "Joueur 2" if players[1] == "" else players[1]
        ]
        self.__player_texts = [
            StringVar(value=f"{self.__player_names[0]}: 0/{self.__pawns_to_win} pions"),
            StringVar(value=f"{self.__player_names[1]}: 0/{self.__pawns_to_win} pions")
        ]
        self.__player_labels = [
            Label(self.__scoreboard, textvariable=self.__player_texts[0], font=DEFAULT_FONT, padx=10).pack(),
            Label(self.__scoreboard, textvariable=self.__player_texts[1], font=DEFAULT_FONT, padx=10).pack()
        ]
        self.__turn_text = StringVar(value=f"Tour 1\n{self.__player_names[0]}, c'est votre tour !")
        Label(self.__scoreboard, textvariable=self.__turn_text, font=DEFAULT_FONT, pady=30).pack()

        self.__drawn_shapes = {}

        self.__draw_board()

    def run(self):
        self.__root.mainloop()

    def __draw_board(self) -> None:
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
    
    def update_labels(self, pawns_out: tuple, turn: int) -> None:
        for i in range(2):
            self.__player_texts[i].set(f"{self.__player_names[i]}: {pawns_out[i]}/{self.__pawns_to_win} pions")
        self.__turn_text.set(f"Tour {turn}\n{self.__player_names[(turn + 1) %2]}, c'est votre tour !")

    def select(self, x: int, y: int, color = "white") -> None:
        shape = self.__canvas.create_oval(X_OFFSETS[x] + y * 66.5 - 4 + GRID_OFFSET[0],
                                          H * x - 4 + GRID_OFFSET[1],
                                          X_OFFSETS[x] + y * 66.5 + 4 + GRID_OFFSET[0],
                                          H * x + 4 + GRID_OFFSET[1],
                                          fill=color, width=0)
        self.__drawn_shapes[f"select={x};{y}"] = shape

    def deselect(self, x: int, y: int) -> None:
        self.__canvas.delete(self.__drawn_shapes[f"select={x};{y}"])

    def get_color_scheme(self) -> dict:
        return self.__color_scheme

    def show_victory_screen(self, winner: int, stalemate = False) -> bool:
        if stalemate:
            showinfo("Yinsh", "Égalité !")
        else:
            showinfo("Yinsh", f"{self.__player_names[winner]} a gagné la partie !")
        replay=askyesno("Yinsh", "Voulez-vous rejouer ?")
        return replay

    def kill(self):
        self.__root.destroy()

class YinshMenu():
    def __init__(self) -> None:
        self.__game_settings=None
        self.__root=Tk()

        self.__root.iconbitmap("icon.ico")
        self.__root.title("Lanceur Yinsh")
        self.__root.resizable(False, False)

        logo_file = PhotoImage(file="logo.png")
        logo_label = Label(self.__root, image=logo_file)
        logo_label.image = logo_file
        logo_label.pack()

        usernames=Frame(self.__root, pady=20)
        usernames.pack()

        Label(usernames,text="Joueur 1 :", padx=10).pack(side="left")
        self.__nomJoueur1=StringVar()
        self.__nomJoueur1.trace_add("write", self.__check_length)
        self.__champJoueur1=Entry(usernames, width=20, textvariable=self.__nomJoueur1)
        self.__champJoueur1.pack(side="left")

        Label(usernames,text="Joueur 2 :", padx=10).pack(side="left")
        self.__nomJoueur2=StringVar()
        self.__nomJoueur2.trace_add("write", self.__check_length)
        self.__champJoueur2=Entry(usernames, width=20, textvariable=self.__nomJoueur2)
        self.__champJoueur2.pack(side="left")

        settings=Frame(self.__root, pady=10)
        settings.pack()

        self.__gamemode=StringVar()
        self.__gametype=StringVar()
        self.__gamemode.set("Normal")
        self.__gametype.set("Offline")
        self.__gm_menu=OptionMenu(settings, self.__gamemode, "Normal", "Blitz")
        self.__gm_menu.pack(side="left", padx=10)
        self.__gt_menu=OptionMenu(settings, self.__gametype, "Offline", "Solo", command=self.__on_change_gametype)
        self.__gt_menu.pack(side="left", padx=10)

        Button(self.__root, text="JOUER", width="11", height="1", font=font.Font(family="Helvetica",size=20,weight="bold"), bg="#657082", fg="white", activebackground="#576170", activeforeground="white", command=self.__launch).pack()

        self.__root.mainloop()
    
    def __check_length(self, var, index, mode):
        nomJoueur = self.__nomJoueur1 if var == "PY_VAR0" else self.__nomJoueur2
        if len(nomJoueur.get())<=15:
            return
        else:
            nomJoueur.set(nomJoueur.get()[0:15])

    def __on_change_gametype(self, _):
        if self.__gametype.get()=="Solo":
            self.__champJoueur2.configure(state=DISABLED)
            self.__nomJoueur2.set("")
        else :
            self.__champJoueur2.configure(state=NORMAL)

    def __launch(self):
        gamemode=self.__gamemode.get()
        gametype=self.__gametype.get()
        self.__game_settings={"gamemode":gamemode, "gametype":gametype, "players":[self.__nomJoueur1.get(), self.__nomJoueur2.get()]}
        if self.__gametype.get() == "Solo":
            self.__game_settings["players"] = [self.__nomJoueur1.get(), "Ordinateur"]
        self.__root.destroy()

    def get_settings(self):
        return self.__game_settings