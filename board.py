"""
CLASSE BOARD
Gestion du plateau de jeu et des règles de déplacement des pions
"""

class YinshBoard():
    def __init__(self) -> None:
        self.__board = [
            [None,0   ,0   ,0   ,0   ,None,None,None,None,None,None],
            [0   ,0   ,0   ,0   ,0   ,0   ,0   ,None,None,None,None],
            [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,None,None,None],
            [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,None,None],
            [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,None],
            [None,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,None],
            [None,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
            [None,None,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
            [None,None,None,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
            [None,None,None,None,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
            [None,None,None,None,None,None,0   ,0   ,0   ,0   ,None]
        ]