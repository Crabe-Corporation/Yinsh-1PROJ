# Yinsh
Classe principale du jeu, gère l'entièreté de l'exécution du jeu dés le démarrage du programme (menu principal, boucle de jeu, etc).
## Paramètres
Les paramètres sont passées via **params pour passer les arguments en keyword arguments à la classe Yinsh.
- gamemode (str)<br>
  Le mode de jeu utilisé pour la partie. Peut prendre la valeur "Normal" pour une partie en 3 points ou "Blitz" pour une partie en 1 point.
- gametype (str)<br>
  Type de partie. Peut prendre la valeur "Online" pour une partie en réseau, "Offline" pour une partie 1 contre 1 en local (sur la même machine) ou "Solo" pour une partie contre l'ordinateur.
- players (list)<br>
  Noms des joueurs.
## Variables
- private gamemode (str) : Mode de jeu récupéré depuis les arguments
- private gametype (str) : Type de partie récupéré depuis les arguments
- private players_names (list) : Noms des joueurs
- private ui (YinshUI) : Composant interface graphique du jeu
- private board (YinshBoard) : Composant plateau utilisée pour la partie
- private pawns_out (tuple[int]) : nombre de pions retirés du plateau pour chaque joueur
- private turn (int) : Compteur de tours de la partie
- private focused (tuple) : Coordonnées du pion sélectionné pour un déplacement. Défini à `None` au début de la partie ou si aucun pion n'est sélectionné.
- private alignment_mode (bool) : Défini à `True` si un joueur est en train de retirer un alignement du plateau de jeu.
- private pawn_removal_mode (bool) : Même principe que alignment_mode, mais pour traquer si un joueur doit retirer un de ses pions.
- private selected_markers (list) : Liste des marqueurs sélectionnés lorsque le joueur retire ses marqueurs après un alignement
- private valid_markers (list) : Variable utilisée pour stocker les coordonnées des marqueurs pouvant être retirés du plateau de jeu lors d'un alignement
- private replay (bool) : Défini à `True` si le joueur veut relancer une nouvelle partie
- private possible_moves (list) : Enregistre les déplacements possibles pour effacer les points servant à visualiser les mouvements possibles d'un pion sur le plateau
- private ai_pawns (list) : Liste des pions du joueur IA dans une partie en mode solo
## Méthodes
- public handle_click(self, x: int, y: int) -> None: fonction appelée par la classe YinshUI lorsqu'un joueur clique sur le plateau de jeu pour gérer la logique du jeu.
- private next_turn(self, check_board: bool) -> bool: exécute toutes les fonctions de la fin du tour et incrémente le compteur `self.__turn`. Si un alignement est découvert, la fonction va attendre que le joueur sélectionne 5 marqueurs à retirer du plateau (ainsi qu'un de ses pions) avant d'incrémenter le compteur de tours. Vérification de la grille uniquement si l'argument check_board est défini à `True`
- private check_for_victory(self) -> bool: Affiche l'écran de victoire si un joueur a sorti le bon nombre de pions du plateau et renvoie `True` si la partie est terminée
- public do_replay(self) -> bool : Retourne la variable replay pour relancer le jeu si le joueur l'a demandé