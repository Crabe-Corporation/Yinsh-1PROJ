# YinshPawn
*from pawn import YinshPawn*<br>
Stockage des données d'un pion sur le plateau.
## Paramètres
- player (int)<br>
  Enregistre le numéro du joueur qui possède le pion (0 correspond au joueur 1 et 1 correspond au joueur 2)
- type (str)<br>
  Type de pion sur le plateau. Peut prendre une des valeurs suivantes : "pawn" pour symboliser un pion qui peut être déplacé par le joueur ou "marking" pour symboliser un marquage laissé par un pion de type "pawn"
## Variables
- private player (int) : numéro du joueur, sauvegardé depuis les paramètres de la fonction `__init__` (0 ou 1)
- private pawn_type (str) : type de pion, sauvegardé depuis les paramètres de la fonction `__init__` ("pawn" ou "marking")
## Méthodes
- public get_pawn_type(self) -> str: getter permettant de récupérer le type de pion ("pawn" ou "marking")
- public get_player(self) -> int : getter qui renvoie le numéro du joueur auquel appartient le pion (0 ou 1)
- public invert_player(self) -> int : inverse le joueur possédant le pion, si ce pion est un marqueur. Renvoie le numéro du joueur mis à jour, ou `False` si le pion n'est pas un marqueur