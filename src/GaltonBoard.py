from src.DropPolicies.BaseDropPolicy import BaseDropPolicy 
import math

class GaltonBoard:

    trays = []
    bullets = []
    dropPolicy = None;

    def __init__(self, trays, bullets, dropPolicy):
        self.trays = trays;
        self.bullets = bullets;
        self.dropPolicy = dropPolicy;

    def _getResultTray(self, bullet):
        position = bullet.getPosition();
        middle = self._middle();
        trayPosition = int(math.floor(middle + position));
        for tray in self.trays:
            if tray.getNumber() == trayPosition:
                return tray;
        raise Exception("Cannot find tray for position " + repr(trayPosition));

    def _updateTray(self, oldTray, newTray):
        newTrays = self.trays;
        key = 0;
        for tray in newTrays:
            if tray == oldTray:
                newTrays[key] = newTray;
            key = key + 1;
        return GaltonBoard(newTrays, self.bullets, self.dropPolicy);

    def _dropBullet(self, bullet):
        for x in range(self._numberOfDrops()):
            if self.dropPolicy.direction() == BaseDropPolicy.LEFT:
                bullet = bullet.dropLeft();
            else: 
                bullet = bullet.dropRight();
        tray = self._getResultTray(bullet);
        return self._updateTray(tray, tray.withBullet(bullet));

    def _middle(self):
        return len(self.trays) / 2;

    def _numberOfDrops(self):
        return len(self.trays) - 1;

    def dropBullets(self):
        galtonboard = self;
        for bullet in self.bullets:
            galtonboard = galtonboard._dropBullet(bullet);
        return galtonboard; 

    def getTrays(self):
        return self.trays;