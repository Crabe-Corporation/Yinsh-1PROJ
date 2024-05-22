# YinshUI
*from ui import YinshUI*<br>
La classe YinshUI s'occupe de gérer l'interface utilisateur d'une partie en cours.
## Paramètres
- gamemode (str)<br>
  Le mode de jeu utilisé pour la partie. Peut prendre la valeur "Normal" pour une partie en 3 points ou "Blitz" pour une partie en 1 point.
- gametype (str)<br>
  Type de partie. Peut prendre la valeur "Online" pour une partie en réseau, "Offline" pour une partie 1 contre 1 en local (sur la même machine) ou "Solo" pour une partie contre l'ordinateur.
<br>
Si l'un de ces paramètres n'est pas valide, la classe renvoie une ValueError.
## Variables
- private game_settings (dict) : contient les paramètres de la partie (deux clés : "blitz_mode" et "online", contenant des booléens)
- private root (Tk) : fenêtre de jeu Tkinter principale
- private canvas (Canvas) : affichage de la grille de jeu
- private scoreboard (Frame) : frame contenant les informations de la partie en cours (joueurs, pions retirés, etc)
- private player_texts (list[StringVar]) : stockage des StringVar pour l'affichage des informations relatives aux joueurs
- private player_labels (list[Label]) : enregistrement des Label affichant les joueurs
- private color_scheme (dict) : thème de couleur enregistré dans un dictionnaire pour les couleurs des pions
## Méthodes
- public draw_board(self) -> None : affichage de la grille sur le canvas
- public draw_pawn(self, x: int, y: int, pawn: YinshPawn) -> int : création d'une nouvelle représentation d'un pion sur le canvas, en utilisant les coordonnées x et y sur la grille et en récupérant les informations depuis une instance de YinshPawn. Renvoie la référence de la forme ajoutée sur le canvas.
- private handle_click(self, event) -> None : fonction appelée lorsque l'utilisateur clique dans le canvas. Utilise la fonction `find_closest_point` depuis le fichier board.py pour traduire les coordonnées du canvas en coordonnées sur la grille