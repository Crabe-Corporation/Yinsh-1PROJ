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
        try:
            if x < 0 or x > 10:
                return False
            if y < 0 or x > 10:
                return False
            if self.__board[x][y] == None:
                return False
            return True
        except IndexError:
            return False
    
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
    
    def get_pawn(self, x: int, y: int) -> YinshPawn:
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
                pawn: YinshPawn = self.__board[x][y]
                if pawn.get_pawn_type() == "marking":
                    new_player = pawn.invert_player()
                    self.__ui.set_color(x, y, new_player)

    def remove_pawn(self, x: int, y: int) -> bool:
        if not self.is_empty(x, y):
            self.__board[x][y] = 0
            self.__ui.erase_pawn(x, y)
            return True
        return False

    def check_board_for_alignment(self) -> list:
        # Lister tous les alignements présents sur le plateau
        alignments = []
        for x in range(11):
            for y in range(11):
                if self.__board[x][y] not in (None, 0):
                    pawn: YinshPawn = self.__board[x][y]
                    if pawn.get_pawn_type() == "marking":
                        new_alignments = self.__check_nearby_intersections(x, y, pawn.get_player())
                        alignments.extend(new_alignments)

        # Récupérer toutes les coordonnées de marqueurs pouvant être retirés
        coordinates = [[],[]] # Séparation des marqueurs du joueur 1 et du joueur 2
        for alignment in alignments:
            for intersection in alignment["markers"]:
                if intersection not in coordinates[self.__board[intersection[0]][intersection[1]].get_player()]:
                    coordinates[self.__board[intersection[0]][intersection[1]].get_player()].append(intersection)

        return coordinates if len(alignments) > 0 else None

    def __check_nearby_intersections(self, x: int, y: int, player: int) -> list:
        alignments = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx, dy) not in ((0, 0), (1, -1), (-1, 1)):
                    if self.is_valid(x + dx, y + dy) and self.__board[x+dx][y+dy] not in (None, 0) and self.__board[x+dx][y+dy].get_player() == player and self.__board[x+dx][y+dy].get_pawn_type() == "marking":
                        length = self.__check_alignment_length(x, y, (dx, dy), 1, player)
                        if length >= 5:
                            alignments.append({"origin": (x, y), "direction": (dx, dy), "length": length, "player": player, "markers": [(x + dx * i, y + dy * i) for i in range(length)]})
        return alignments

    def __check_alignment_length(self, x: int, y: int, direction: tuple, length: int, player: int, intersections = []) -> int:
        if self.is_valid(x + direction[0], y + direction[1]) and not self.is_empty(x + direction[0], y + direction[1]):
            pawn: YinshPawn = self.__board[x + direction[0]][y + direction[1]]
            if pawn.get_pawn_type() == "marking" and pawn.get_player() == player:
                return self.__check_alignment_length(x + direction[0], y + direction[1], direction, length + 1, player)
        return length

    def get_possible_moves(self, x: int, y: int) -> list:
        if self.is_empty(x, y):
            return []
        
        pawn: YinshPawn = self.__board[x][y]
        if pawn and pawn.get_pawn_type() == "marking":
            return []
        
        coordinates = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx, dy) not in ((0, 0), (1, -1), (-1, 1)):
                    distance = 1
                    while True:
                        new_x, new_y = x + (dx * distance), y + (dy * distance)
                        if self.is_valid(new_x, new_y):
                            if self.can_move(x, y, new_x, new_y):
                                coordinates.append((new_x, new_y))
                            distance += 1
                        else:
                            break
        
        return coordinates
    
    def is_blocked(self, x: int, y: int) -> bool:
        return self.get_possible_moves(x, y) == []
    
    def is_player_blocked(self, player: int) -> bool:
        for x in range(11):
            for y in range(11):
                if self.__board[x][y] and not self.is_empty(x, y) and not self.is_blocked(x, y) and self.__board[x][y].get_player() == player:
                    return False
        return True
    
    def is_everyone_blocked(self) -> bool:
        for x in range(11):
            for y in range(11):
                if not self.is_empty(x, y) and not self.is_blocked(x, y):
                    return False
        return True


def generate_empty_board() -> list:
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

def find_closest_point(x: int, y: int) -> tuple:
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