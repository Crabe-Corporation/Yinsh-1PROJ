"""
CLASSE BOARD
Gestion du plateau de jeu et des règles de déplacement des pions
"""

"""
Offsets en X sur le canvas
Chaque nombre correspond aux coordonnées x du point (i, 0), où i correspond à l'index dans le tuple X_OFFSET
Ces offsets ne prennent pas en compte les marges autour de la grille dans l'interface utilisateur
"""
from math import sqrt
H = 66.5 * sqrt(3) / 2
X_OFFSETS = (
    133,
    99.75,
    66.5,
    33.25,
    0,
    -33.25,
    -66.5,
    -99.75,
    -133,
    -166.25,
    -199.5
)

"""
YinshBoard()
Tableau : None = case invalide, 0 = case vide, YinshPawn = pion d'un joueur
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