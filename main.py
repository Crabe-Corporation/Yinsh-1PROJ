from ui import YinshUI

"""
Yinsh()
Classe principale du jeu
"""
class Yinsh():
    def __init__(self, **params) -> None:
        if "gamemode" in params.keys() and "gametype" in params.keys():
            ui = YinshUI(**params)
        else:
            raise KeyError("la classe Yinsh a besoin des paramètres gamemode et gametype pour fonctionner !")

if __name__ == "__main__":
    game = Yinsh(gamemode="Blitz", gametype="Offline")