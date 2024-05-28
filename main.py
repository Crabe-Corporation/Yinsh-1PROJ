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
            self.__pawns_out = [0, 0]
            self.__turn = 1
            self.__focused = None
            self.__alignment_mode = False
            self.__pawn_removal_mode = False
            self.__selected_markers = []
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

            if self.__pawn_removal_mode:
                print("REMOVE PAWN")
                pawn: YinshPawn = self.__board.get_pawn(x, y)
                if pawn and pawn.get_pawn_type() == "pawn" and pawn.get_player() == (self.__turn + 1) %2:
                    self.__board.remove_pawn(x, y)
                    self.__pawns_out[(self.__turn + 1) %2] += 1
                    self.__pawn_removal_mode = False
                    self.__check_for_victory()
                    if not self.__board.check_board_for_alignment():
                        self.__alignment_mode = False
                        self.__next_turn(board_check=True)
                return

            if self.__alignment_mode:
                print("ALIGNMENT")
                # Sélectionner / désélectionner un marqueur
                if (x, y) in self.__valid_markers:
                    if (x, y) not in self.__selected_markers:
                        self.__ui.select(x, y)
                        self.__selected_markers.append((x, y))
                    else:
                        self.__ui.deselect(x, y)
                        self.__selected_markers.remove((x, y))
                
                # Si 5 marqueurs sont sélectionnés, vérifier qu'ils forment bien un alignement
                if len(self.__selected_markers) >= 5:
                    low = min(self.__selected_markers)
                    high = max(self.__selected_markers)
                    if (abs(high[0] - low[0]), abs(high[1] - low[1])) in ((4,0),(0,4),(4,4)):
                        # Alignement valide
                        for coordinates in self.__selected_markers:
                            self.__board.remove_pawn(coordinates[0], coordinates[1])

                    # Effacer la sélection de l'interface utilisateur
                    for coordinates in self.__selected_markers:
                        self.__ui.deselect(coordinates[0], coordinates[1])
                    self.__selected_markers = []

                    self.__pawn_removal_mode = True
                    


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
    
    def __check_for_victory(self) -> bool:
        threshold = 1 if self.__gamemode == "Blitz" else 3
        for player in range(2):
            if self.__pawns_out[player] >= threshold:
                self.__ui.update_labels(self.__pawns_out, self.__turn)
                self.__replay=self.__ui.show_victory_screen(player)
                self.__ui.kill()

    def do_replay(self) -> bool:
        return self.__replay

if __name__ == "__main__":
    while True:
        menu=YinshMenu()
        settings=menu.get_settings()
        game = Yinsh(**settings)
        if not game.do_replay():
            break