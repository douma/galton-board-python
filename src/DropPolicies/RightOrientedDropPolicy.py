from src.DropPolicies.BaseDropPolicy import BaseDropPolicy 

class RightOrientedDropPolicy(BaseDropPolicy):

    def direction(self):
        return self.RIGHT;
