from src.DropPolicies.BaseDropPolicy import BaseDropPolicy 

class LeftRightDropPolicy(BaseDropPolicy):

    def __init__(self):
        self.position = self.LEFT;

    def direction(self):
        if self.position == self.RIGHT:
            self.position = self.LEFT;
            return self.LEFT;
        else:
            self.position = self.RIGHT;
            return self.RIGHT;
