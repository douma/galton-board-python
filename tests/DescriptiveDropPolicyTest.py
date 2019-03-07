import unittest
from src.DropPolicies.DescriptiveDropPolicy import DescriptiveDropPolicy
from src.DropPolicies.BaseDropPolicy import BaseDropPolicy

class DescriptiveDropPolicyTest(unittest.TestCase):

    def test_should_return_from_words(self):
        dropPolicy = DescriptiveDropPolicy("left,right,left");
        self.assertEqual(BaseDropPolicy.LEFT, dropPolicy.direction());
        self.assertEqual(BaseDropPolicy.RIGHT, dropPolicy.direction());
        self.assertEqual(BaseDropPolicy.LEFT, dropPolicy.direction());

if __name__ == '__main__':
    unittest.main()