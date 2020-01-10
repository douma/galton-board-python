class Tray:

    def __init__(self, number):
        self.number = number;
        self.bullets = [];

    @staticmethod 
    def listFromLength(length):
        trays = [];
        for x in range(length):
            trays.append(Tray(x));
        return trays;

    def withBullet(self, bullet):
        newBullets = list(self.bullets);
        newBullets.append(bullet);
        newTray = Tray(self.number);
        newTray.bullets = newBullets;
        return newTray;

    def getNumber(self):
        return self.number;

    def numberOfBullets(self):
        return len(self.bullets);
