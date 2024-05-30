# YinshMenu
*from ui import YinshMenu*<br>
Création et affichage du menu principal.
## Paramètres
Aucun paramètre.
## Variables
- private root (Tk) : Fenêtre du menu principal
- private game_settings (dict) : Stockage des paramètres de la partie
- private nomJoueur1 (StringVar) : Nom du joueur 1
- private champJoueur1 (Entry) : Champ de texte pour inscrire le nom du joueur 1
- private nomJoueur2 (StringVar) : Nom du joueur 2
- private champJoueur2 (Entry) : Champ de texte pour inscrire le nom du joueur 2
- private gamemode (StringVar) : Stockage du mode de jeu (Normal/Blitz)
- private gametype (StringVar) : Stockage du type de jeu (Offline/Solo)
- private gm_menu (OptionMenu) : Menu déroulant des modes de jeu
- private gt_menu (OptionMenu) : Menu déroulant des types de jeu
## Méthodes
- private check_length(self, var, index, mode) -> None: vérifie la longueur du pseudo des utilisateurs lorsque l'utilisateur met à jour les champs de texte et annule la modification si le pseudo est trop long. Longueur limite du pseudo : 15 caractères.
- private on_change_gametype(self, _) -> None: désactive et efface l'input du joueur 2 quand le mode Solo est sélectionné dans le menu déroulant.
- private launch(self) -> None :
Enregistre les paramètres et ferme la fenêtre.
- public get_settings(self) -> dict :
Renvoie les paramètres de la partie hors de la classe pour lancer le jeu.