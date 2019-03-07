import unittest
import sys
from src.Tray import Tray 
from src.Bullet import Bullet 

class TrayTest(unittest.TestCase):

    def test_tray_should_be_constructed_from_length(self):
        trays = Tray.listFromLength(10);
        self.assertEqual(10, len(trays));

    def test_withBullet_should_return_new_instance(self):
        trays = Tray.listFromLength(10);
        tray = trays[0];
        newTray = tray.withBullet(Bullet(0));
        self.assertNotEqual(newTray, Tray);
        self.assertNotEqual(newTray.numberOfBullets(), tray.numberOfBullets());

if __name__ == '__main__':
    unittest.main()