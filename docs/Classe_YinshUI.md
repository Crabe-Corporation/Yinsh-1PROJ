# YinshUI
*from ui import YinshUI*<br>
La classe YinshUI s'occupe de gérer l'interface utilisateur d'une partie en cours.
## Paramètres
- settings (tuple)<br>
  Paramètres de la partie en cours enregistrés avec 2 booléens. Le premier paramètre active le mode Blitz si défini à `True`, le second paramètre indique si la partie à été lancée en mode réseau (`True` = mode en ligne, `False` = partie locale)
## Variables
- private game_settings (dict) : contient les paramètres de la partie (deux clés : "blitz_mode" et "online", contenant des booléens)
- private root (Tk) : fenêtre de jeu Tkinter principale
- private canvas (Canvas) : affichage de la grille de jeu
- private scoreboard (Frame) : frame contenant les informations de la partie en cours (joueurs, pions retirés, etc)
## Méthodes
- public draw_board(self) -> None : affichage de la grille sur le canvas