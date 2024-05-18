"""
CLASSE PAWN
Pions présents sur le plateau de jeu
"""

class YinshPawn():
    def __init__(self, player: int, type: str) -> None:
        self.__player = player
        self.__pawn_type = type