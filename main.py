from ui import YinshUI
from pawn import YinshPawn
from board import YinshBoard

"""
Yinsh()
Classe principale du jeu
"""
class Yinsh():
    def __init__(self, **params) -> None:
        if not "gamemode" in params.keys() or "gametype" not in params.keys():
            raise KeyError("la classe Yinsh a besoin des paramètres gamemode et gametype pour fonctionner !")
        else:
            self.__gamemode = params["gamemode"]
            self.__gametype = params["gametype"]
            self.__ui = YinshUI(self, **params)
            self.__board = YinshBoard(self.__ui)
            self.__turn = 1
            self.__focused = None

            #! Lancer l'interface graphique du jeu en dernier
            self.__ui.run()

    def handle_click(self, x: int, y: int) -> None:
        if self.__turn <= 10:
            # Tour d'initialisation : placer un pion sur le plateau
            if not self.__board.is_empty(x, y):
                return
            new_pawn = YinshPawn((self.__turn - 1) %2, "pawn")
            if self.__board.place_new_pawn(x, y, new_pawn):
                self.__turn += 1
        else:
            # Tour classique : déplacer un pion et créer un marqueur
            if not self.__focused:
                pawn = self.__board.get_pawn(x, y)
                if not pawn:
                    return
                if pawn.get_player() != (self.__turn - 1) %2:
                    return
                self.__focused = (x, y)
            else:
                x_start ,y_start = self.__focused
                if x_start == x and y_start == y:
                    # Annulation
                    self.__focused = None
                if self.__board.can_move(x_start, y_start, x, y):
                    self.__board.move_pawn(x_start, y_start, x, y)
                    self.__focused = None
                    self.__turn += 1
                else:
                    pass


if __name__ == "__main__":
    game = Yinsh(gamemode="Blitz", gametype="Offline")