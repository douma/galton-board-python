from src.DropPolicies.BaseDropPolicy import BaseDropPolicy 
import random;

class RandomDropPolicy(BaseDropPolicy):

    def direction(self):
        randomBool = bool(random.getrandbits(1))
        if(randomBool == 1):
            return self.RIGHT;
        else:
            return self.LEFT;