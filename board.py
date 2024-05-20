from math import sqrt

"""
CLASSE BOARD
Gestion du plateau de jeu et des règles de déplacement des pions
"""

"""
Offsets en X sur le canvas
Chaque nombre correspond aux coordonnées x du point (i, 0), où i correspond à l'index dans le tuple X_OFFSET
Ces offsets ne prennent pas en compte les marges autour de la grille dans l'interface utilisateur
"""
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
        self.__board = generate_empty_board()

def generate_empty_board() -> list[list[int | None]]:
    return [
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

def find_closest_point(x: int, y: int) -> tuple[int]:
    from ui import GRID_OFFSET
    
    # Calculer toutes les coordonnées des intersections du plateau
    mask = generate_empty_board()
    coordinates = []
    for grid_x in range(11):
        for grid_y in range(11):
            if mask[grid_x][grid_y] != None:
                dist_x = abs(x - (X_OFFSETS[grid_x] + grid_y * 66.5 + GRID_OFFSET[0]))
                dist_y = abs(y - (H * grid_x + GRID_OFFSET[1]))
                coordinates.append({
                    "grid_x": grid_x,
                    "grid_y": grid_y,
                    "distance": sqrt(dist_x ** 2 + dist_y ** 2)
                })
    
    # Parcourir cette liste de coordonnées pour chercher le point le plus proche
    dist_min = coordinates[0]["distance"]
    index = 0
    for i in range(len(coordinates) - 1):
        if dist_min > coordinates[i + 1]["distance"]:
            dist_min = coordinates[i + 1]["distance"]
            index = i + 1

    # Retourner les coordonnées du point le plus proche
    return (coordinates[index]["grid_x"], coordinates[index]["grid_y"])