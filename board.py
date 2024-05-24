from math import sqrt
from pawn import YinshPawn

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
    def __init__(self, ui) -> None:
        self.__board = generate_empty_board()
        self.__ui = ui

    def is_valid(self, x: int, y: int) -> bool:
        if x < 0 or x > 11:
            return False
        if y < 0 or x > 11:
            return False
        if self.__board[x][y] == None:
            return False
        return True
    
    def is_empty(self, x: int, y: int) -> bool:
        if not self.is_valid(x, y):
            return False
        if self.__board[x][y] != 0:
            return False
        return True
    
    def can_move(self, x_start: int, y_start: int, x_end: int, y_end: int)  -> bool:
        # Vérifier que la case est sur l'un des 6 axes possibles
        if x_start != x_end and y_start != y_end:
            if (x_end - x_start != y_end - y_start):
                return False
            
        # Vérifier si la destination est occupée ou non
        if not self.is_empty(x_end, y_end):
            return False
        
        # Vérifier si les règles de déplacement par dessus des marquages sont respectées
        distance = abs(x_end - x_start) if abs(x_end - x_start) != 0 else abs(y_end - y_start)
        dist_x, dist_y = x_end - x_start, y_end - y_start
        x, y = x_start, y_start
        marking_found = False
        while x != x_end or y != y_end:
            # Se déplacer d'une intersection vers la destination
            x += dist_x // distance
            y += dist_y // distance

            # Vérifier la case
            if self.is_empty(x, y) and not marking_found:
                pass
            else:
                if self.is_empty(x, y) and marking_found and (x != x_end or y != y_end):
                    return False
                if self.is_empty(x, y) and marking_found and x == x_end and y == y_end:
                    break
                if self.__board[x][y].get_pawn_type() == "pawn":
                    return False
                if self.__board[x][y].get_pawn_type() == "marking":
                    marking_found = True
        return True
    
    def get_pawn(self, x: int, y: int) -> YinshPawn | None:
        if self.is_empty(x, y):
            return None
        return self.__board[x][y]
    
    def place_new_pawn(self, x: int, y: int, pawn: YinshPawn) -> bool:
        if not self.is_empty(x, y):
            return False
        self.__board[x][y] = pawn
        self.__ui.draw_pawn(x, y, pawn)
        return True
    
    def move_pawn(self, x_start: int, y_start: int, x_end: int, y_end: int) -> None:
        # Déplacer le pawn aux nouvelles coordonnées
        old_pawn = self.__board[x_start][y_start]
        self.__board[x_start][y_start] = 0
        self.__ui.erase_pawn(x_start, y_start)
        self.place_new_pawn(x_start, y_start, YinshPawn(old_pawn.get_player(), "marking"))
        self.place_new_pawn(x_end, y_end, old_pawn)

        # Retourner tous les marqueurs
        distance = abs(x_end - x_start) if abs(x_end - x_start) != 0 else abs(y_end - y_start)
        dist_x, dist_y = x_end - x_start, y_end - y_start
        x, y = x_start, y_start
        while x != x_end or y != y_end:
            x += dist_x // distance
            y += dist_y // distance

            if not self.is_empty(x, y):
                pawn = self.__board[x][y]
                if pawn.get_pawn_type() == "marking":
                    new_player = pawn.invert_player()
                    self.__ui.set_color(x, y, new_player)

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