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
            self.__board = YinshBoard()
            self.__turn = 1
            self.__focused = None

            #! Lancer l'interface graphique du jeu en dernier
            self.__ui.run()

    def handle_click(self, x: int, y: int) -> None:
        print(f"Tour {self.__turn}")
        if self.__turn <= 10:
            # Tour d'initialisation : placer un pion sur le plateau
            if not self.__board.is_empty(x, y):
                return
            new_pawn = YinshPawn((self.__turn - 1) %2, "pawn")
            if self.__board.place_new_pawn(x, y, new_pawn):
                self.__ui.draw_pawn(x, y, new_pawn)
                self.__turn += 1
        else:
            # Tour classique : déplacer un pion et créer un marqueur
            if not self.__focused:
                pawn = self.__board.get_pawn(x, y)
                if not pawn:
                    return
                if pawn.get_player() != (self.__turn - 1) %2:
                    return
                print(f"Pion ({x};{y}) sélectionné !")
                self.__focused = (x, y)
            else:
                x_start ,y_start = self.__focused
                print(f"Tentative de déplacement de ({x_start};{y_start}) vers ({x};{y})")
                if self.__board.can_move(x_start, y_start, x, y):
                    print("Good !")
                    self.__focused = None
                    self.__turn += 1
                else:
                    print("Not good !")


if __name__ == "__main__":
    game = Yinsh(gamemode="Blitz", gametype="Offline")