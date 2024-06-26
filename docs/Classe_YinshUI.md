# YinshUI
*from ui import YinshUI*<br>
La classe YinshUI s'occupe de gérer l'interface utilisateur d'une partie en cours.
## Paramètres
- gamemode (str)<br>
  Le mode de jeu utilisé pour la partie. Peut prendre la valeur "Normal" pour une partie en 3 points ou "Blitz" pour une partie en 1 point.
- gametype (str)<br>
  Type de partie. Peut prendre la valeur "Offline" pour une partie 1 contre 1 en local (sur la même machine) ou "Solo" pour une partie contre l'ordinateur.
- players (list) : Noms des joueurs.
<br>
Si l'un de ces paramètres n'est pas valide, la classe renvoie une ValueError.

## Variables
- private game_settings (dict) : contient les paramètres de la partie (deux clés : "mode" et "type", contenant des booléens)
- private root (Tk) : fenêtre de jeu Tkinter principale
- private canvas (Canvas) : affichage de la grille de jeu
- private scoreboard (Frame) : frame contenant les informations de la partie en cours (joueurs, pions retirés, etc)
- private player_names (list[str]) : stockage des noms des joueurs si définis dans le menu principal
- private player_texts (list[StringVar]) : stockage des StringVar pour l'affichage des informations relatives aux joueurs
- private player_labels (list[Label]) : enregistrement des Label affichant les joueurs
- private color_scheme (dict) : thème de couleur enregistré dans un dictionnaire pour les couleurs des pions
- private drawn_shapes (dict) : contient toutes les représentations de pions sur l'interface utilisateur pour les modifier si besoin. La clé contient les coordonnées sous la forme "x;y" et la valeur correspond à une forme sur le canvas
- private pawns_to_win (int) : nombre de pions à retirer du plateau pour gagner une partie
## Méthodes
- public run(self) -> None : lancement de la fenêtre graphique du jeu
- private draw_board(self) -> None : affichage de la grille sur le canvas
- public draw_pawn(self, x: int, y: int, pawn: YinshPawn) -> int : création d'une nouvelle représentation d'un pion sur le canvas, en utilisant les coordonnées x et y sur la grille et en récupérant les informations depuis une instance de YinshPawn. Renvoie la référence de la forme ajoutée sur le canvas.
- private handle_click(self, event) -> None : fonction appelée lorsque l'utilisateur clique dans le canvas. Utilise la fonction `find_closest_point` depuis le fichier board.py pour traduire les coordonnées du canvas en coordonnées sur la grille
- public erase_pawn(self, x: int, y: int) -> bool : fonction servant à effacer une forme dessinée aux coordonnées (x;y) du plateau. Renvoie `True` si la suppression de la forme a été correctement effectuée
- public set_color(self, x: int, y: int, player: int) -> bool : modifie la couleur d'une forme dessinée aux coordonnées (x;y) du plateau pour correspondre au numéro du joueur passé en paramètre. Renvoie `True` si l'inversion est réussie
- public update_labels(self, pawns_out: tuple[int], turn: int) -> None : met à jour les labels des joueurs et le label du tour en cours. Appelée à chaque tour depuis la classe Yinsh
- public select(self, x: int, y: int, color: str) -> None : ajoute un point (blanc par défaut, modifiable via l'argument color) aux coordonnées (x;y) du plateau de jeu
- public deselect(self, x: int, y: int) -> None : retire un point ajouté par la fonction `select` aux coordonnées (x;y)
- public get_color_scheme(self) -> dict : retourne les couleurs utilisées dans l'interface graphique du jeu
- public show_victory_screen(self, winner: int, stalemate = False) -> bool : affiche l'écran de victoire, demande au joueur si il veut rejouer et renvoie `True` si il sélectionne "Oui"
- public kill(self) -> None : ferme la fenêtre de jeu une fois la partie terminée