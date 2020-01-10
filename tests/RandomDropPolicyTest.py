import unittest
from src.DropPolicies.RandomDropPolicy import RandomDropPolicy 

class RandomDropPolicyTest(unittest.TestCase):

    def test_should_return_left_and_right_random(self):
        randomPolicy = RandomDropPolicy();
        firstDirection = randomPolicy.direction();
        nextDirection = randomPolicy.direction();
        while(nextDirection == firstDirection):
            nextDirection = randomPolicy.direction();
        self.assertNotEqual(firstDirection, nextDirection);

if __name__ == '__main__':
    unittest.main()