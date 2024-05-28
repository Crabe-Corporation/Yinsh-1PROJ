# YinshBoard
*from board import YinshBoard*<br>
Gestion complète du plateau de jeu et des déplacements des pions.
## Paramètres
- ui (YinshUI)<br>
  Composant Interface Utilisateur lié au board pour la mise à jour de la fenêtre de jeu à chaque changement sur le plateau
## Variables
- private board (list) : stockage de la grille de jeu sous la forme d'une liste en 2 dimensions
## Méthodes
- public is_valid(self, x: int, y: int) -> bool: vérifie si les coordonnées x et y renseignées sont des coordonnées valides sur un plateau de Yinsh. Renvoie `True` si c'est le cas, sinon `False`.
- public is_empty(self, x: int, y: int) -> bool: vérifie si l'intersection aux coordonnées (x;y) est vide ou non. Renvoie `True` si la case est vide (0) et `False` si la case est occupée ou invalide.
- public can_move(self, x_start: int, y_start: int, x_end: int, y_end: int) -> bool: Vérifie si le mouvement de (x_start;y_start) vers (x_end;y_end) est possible et renvoie le résultat en booléen.
- public get_pawn(self, x: int, y: int) -> YinshPawn | None: renvoie le pion présent sur le plateau de jeu aux coordonnées (x;y), ou `None` si la case est vide.
- public place_new_pawn(self, x: int, y: int, pawn: YinshPawn) -> bool: place un nouveau pion dans la variable self.__board (plateau logique) si les conditions sont remplies. Renvoie un booléen pour indiquer si l'ajout du pion sur le plateau est un succès.
- public move_pawn(self, x_start: int, y_start: int, x_end: int, y_end: int) -> None: déplace un pion depuis les coordonnées (x_start;y_start) vers les coordonnées (x_end;y_end) en faisant les modifications nécessaires au plateau (changements de couleur, ajout d'un marqueur)
- public remove_pawn(self, x: int, y: int) -> bool: retire un pion/marqueur du plateau de jeu. Renvoie `True` si l'opération est réussie, sinon `False`
- public check_board_for_alignment(self) -> list[dict]: fonction servant à détecter un alignement sur le plateau de jeu. Renvoie la liste de tous les marqueurs pouvant être retirés du plateau, ou `None` si aucun alignement n'a été trouvé
- private check_nearby_intersections(self, x: int, y: int, player: int) -> list[dict]: fonction appelée par `check_board_for_alignment`, vérifie toutes les intersections adjacentes et appelle la fonction `check_alignment_length` pour vérifier si 3 autres marqueurs (ou plus) sont présents dans la continuité. Renvoie une liste des alignements de 5 (ou plus) marqueurs du joueur `player` autour du marqueur en (x;y)
- private check_alignment_length(self, x: int, y: int, direction: tuple[int], length: int, player: int, intersections = []) -> int: dans la continuité des fonctions `check_board_for_alignment` et `check_nearby_intersections`, fonction récursive vérifiant la longueur de l'alignement détecté et retournant un entier indiquant le nombre de marqueurs alignés