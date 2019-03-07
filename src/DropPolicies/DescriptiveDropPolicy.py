from src.DropPolicies.BaseDropPolicy import BaseDropPolicy 
import random;

class DescriptiveDropPolicy(BaseDropPolicy):

    words = [];
    index = -1;

    def __init__(self, description):
        self.words = description.split(',');

    def direction(self):
        self.index = self.index + 1;
        return self.words[self.index];