from ui import YinshUI, YinshMenu
from pawn import YinshPawn
from board import YinshBoard

"""
Yinsh()
Classe principale du jeu
"""
class Yinsh():
    def __init__(self, **params) -> None:
        if not "gamemode" in params.keys() or "gametype" not in params.keys() or "players" not in params.keys():
            raise KeyError("la classe Yinsh a besoin des paramètres gamemode et gametype pour fonctionner !")
        else:
            self.__gamemode = params["gamemode"]
            self.__gametype = params["gametype"]
            self.__players_names= (
                "Joueur 1" if params["players"][0] == "" else params["players"][0],
                "Joueur 2" if params["players"][1] == "" else params["players"][1]
            )
            self.__ui = YinshUI(self, **params)
            self.__board = YinshBoard(self.__ui)
            self.__pawns_out = (0, 0)
            self.__turn = 1
            self.__focused = None
            self.__alignment_mode = False
            self.__selected_markers = None
            self.__valid_markers = None

            #! Lancer l'interface graphique du jeu en dernier
            self.__ui.run()

    def handle_click(self, x: int, y: int) -> None:
        if self.__turn <= 10:
            # Tour d'initialisation : placer un pion sur le plateau
            if not self.__board.is_empty(x, y):
                return
            new_pawn = YinshPawn((self.__turn - 1) %2, "pawn")
            if self.__board.place_new_pawn(x, y, new_pawn):
                self.__next_turn()
        else:
            # Tour classique : déplacer un pion et créer un marqueur
            if self.__focused:
                print("MOVE")
                x_start ,y_start = self.__focused
                if x_start == x and y_start == y:
                    # Annulation
                    self.__focused = None
                if self.__board.can_move(x_start, y_start, x, y):
                    self.__board.move_pawn(x_start, y_start, x, y)
                    self.__focused = None
                    self.__next_turn(board_check=True)
                else:
                    pass

            if self.__alignment_mode:
                print("ALIGNMENT")
                pass

            if not self.__focused and not self.__alignment_mode:
                print("SELECT")
                pawn = self.__board.get_pawn(x, y)
                if not pawn:
                    return
                if pawn.get_player() != (self.__turn - 1) %2:
                    return
                self.__focused = (x, y)


    def __next_turn(self, board_check=False) -> bool:
        print("NEXT")
        if board_check:
            coordinates = self.__board.check_board_for_alignment()
            print(coordinates)
            if coordinates and len(coordinates[(self.__turn + 1) %2]) > 0:
                # Alignements trouvés pour le joueur actif
                self.__valid_markers = coordinates[(self.__turn + 1) %2]
                self.__alignment_mode = True
                return True

        self.__turn += 1
        self.__ui.update_labels(self.__pawns_out, self.__turn)
        return False

if __name__ == "__main__":
    menu=YinshMenu()
    settings=menu.get_settings()
    game = Yinsh(**settings)