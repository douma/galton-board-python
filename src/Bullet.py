class Bullet:

    def __init__(self,position):
        self.position = position 

    @staticmethod
    def listFromLength(length):
        balls = [];
        for x in range(length):
            balls.append(Bullet(0));
        return balls;

    def dropLeft(self):
        newPosition = self.position - 0.5
        return Bullet(newPosition);

    def dropRight(self):
        newPosition = self.position + 0.5
        return Bullet(newPosition);

    def getPosition(self):
        return self.position;
