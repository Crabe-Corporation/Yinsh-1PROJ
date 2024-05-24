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
- private turn (int) : Compteur de tours de la partie
- private focused (tuple) : Coordonnées du pion sélectionné pour un déplacement. Défini à `None` au début de la partie ou si aucun pion n'est sélectionné.
## Méthodes
- public handle_click(self, x: int, y: int) -> None: fonction appelée par la classe YinshUI lorsqu'un joueur clique sur le plateau de jeu pour gérer la logique du jeu.