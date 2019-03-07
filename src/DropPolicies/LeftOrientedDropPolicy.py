from src.DropPolicies.BaseDropPolicy import BaseDropPolicy 

class LeftOrientedDropPolicy(BaseDropPolicy):

    def direction(self):
        return self.LEFT;
