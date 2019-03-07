import unittest
import sys
from src.Tray import Tray 
from src.Bullet import Bullet 
from src.GaltonBoard import GaltonBoard 
from src.DropPolicies.LeftOrientedDropPolicy import LeftOrientedDropPolicy 
from src.DropPolicies.RightOrientedDropPolicy import RightOrientedDropPolicy 
from src.DropPolicies.LeftRightDropPolicy import LeftRightDropPolicy 

class GaltonBoardTest(unittest.TestCase):

    def test_should_drop_bullets_to_left_most_tray_and_return_new_galtonboard_instance(self):
        galtonBoard = GaltonBoard(Tray.listFromLength(10), Bullet.listFromLength(100), LeftOrientedDropPolicy());
        newGaltonBoard = galtonBoard.dropBullets();
        self.assertTrue(type(newGaltonBoard) is GaltonBoard);
        self.assertNotEqual(newGaltonBoard, galtonBoard);
        self.assertEquals(100, galtonBoard.getTrays()[0].numberOfBullets());
        self.assertEquals(0, galtonBoard.getTrays()[9].numberOfBullets());

    def test_should_drop_bullets_to_right_most_tray_and_return_new_galtonboard_instance(self):
        galtonBoard = GaltonBoard(Tray.listFromLength(10), Bullet.listFromLength(100), RightOrientedDropPolicy());
        newGaltonBoard = galtonBoard.dropBullets();
        self.assertTrue(type(newGaltonBoard) is GaltonBoard);
        self.assertNotEqual(newGaltonBoard, galtonBoard);
        self.assertEquals(0, galtonBoard.getTrays()[0].numberOfBullets());
        self.assertEquals(100, galtonBoard.getTrays()[9].numberOfBullets());

    def test_should_drop_bullets_to_middle_tray_and_return_new_galtonboard_instance(self):
        galtonBoard = GaltonBoard(Tray.listFromLength(11), Bullet.listFromLength(100), LeftRightDropPolicy());
        newGaltonBoard = galtonBoard.dropBullets();
        self.assertTrue(type(newGaltonBoard) is GaltonBoard);
        self.assertNotEqual(newGaltonBoard, galtonBoard);
        self.assertEquals(0, galtonBoard.getTrays()[0].numberOfBullets());
        self.assertEquals(100, galtonBoard.getTrays()[5].numberOfBullets());
        self.assertEquals(0, galtonBoard.getTrays()[10].numberOfBullets());

if __name__ == '__main__':
    unittest.main()