"""
CLASSE PAWN
Pions présents sur le plateau de jeu
"""

class YinshPawn():
    def __init__(self, player: int, type: str) -> None:
        self.__player = player
        self.__pawn_type = type

    def get_pawn_type(self) -> str:
        return self.__pawn_type
    
    def get_player(self) -> int:
        return self.__player
    
    def invert_player(self) -> int:
        if self.__pawn_type == "pawn":
            return False
        self.__player = (self.__player + 1) %2
        return self.__player