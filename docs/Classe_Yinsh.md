# Yinsh
Classe principale du jeu, gère l'entièreté de l'exécution du jeu dés le démarrage du programme (menu principal, boucle de jeu, etc)
## Paramètres
Les paramètres sont passées via **params pour passer les arguments en keyword arguments à la classe Yinsh.
- gamemode (str)<br>
  Le mode de jeu utilisé pour la partie. Peut prendre la valeur "Normal" pour une partie en 3 points ou "Blitz" pour une partie en 1 point.
- gametype (str)<br>
  Type de partie. Peut prendre la valeur "Online" pour une partie en réseau, "Offline" pour une partie 1 contre 1 en local (sur la même machine) ou "Solo" pour une partie contre l'ordinateur.
## Variables
- private ui (YinshUI) : composant interface utilisateur du jeu
## Méthodes
Aucune méthode