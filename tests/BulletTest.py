import unittest
import sys
from src.Bullet import Bullet 

class BulletTest(unittest.TestCase):

    def test_bullet_should_be_constructed_from_length(self):
        bullets = Bullet.listFromLength(10);
        self.assertEqual(10, len(bullets));

    def test_bullet_should_drop_left(self):
        bullets = Bullet.listFromLength(10);
        bullet = bullets[0]
        bullet = bullet.dropLeft();
        bullet = bullet.dropLeft();
        self.assertEqual(-1,bullet.getPosition())

    def test_bullet_should_drop_right(self):
        bullets = Bullet.listFromLength(10);
        bullet = bullets[0]
        bullet = bullet.dropRight();
        self.assertEqual(0.5,bullet.getPosition())

if __name__ == '__main__':
    unittest.main()