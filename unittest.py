import unittest
import pyglet
from missile import Missile

class TestMissile(unittest.TestCase):
    
    def setUp(self):
        self.window = pyglet.window.Window()
        self.missile = Missile(self.window)
        
    def test_missile_rotation(self):
        self.assertEqual(self.missile.rotation, 90)
        
    def test_missile_placement(self):
        self.assertEqual(self.missile.x, self.window.width / 2)
        self.assertEqual(self.missile.y, self.window.height / 2)
        
    def test_on_draw(self):
        self.missile.on_draw()
        self.assertIsNotNone(self.window.clear())
        self.assertIsNotNone(self.missile.terrain_batch.draw())
        self.assertIsNotNone(self.missile.entity_batch.draw())
        
if __name__ == '__main__':
    unittest.main()