import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.Tray import Tray 
from src.Bullet import Bullet 
from src.GaltonBoard import GaltonBoard 
from src.DropPolicies.RandomDropPolicy import RandomDropPolicy 

class Main:
    @staticmethod
    def run():
        galtonBoard = GaltonBoard(Tray.listFromLength(10), Bullet.listFromLength(250), RandomDropPolicy());
        galtonBoard = galtonBoard.dropBullets();
        for tray in galtonBoard.getTrays():
            print(str("").zfill(tray.numberOfBullets()));

Main.run();
