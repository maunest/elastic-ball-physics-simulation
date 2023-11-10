import unittest
from tkinter import Tk
from unittest.mock import patch
from app.bouncing_ball_simulation import BouncingBallSimulation


class TestBouncingBallSimulation(unittest.TestCase):
    def setUp(self):
        self.root = Tk()

    def tearDown(self):
        self.root.destroy()

    def test_create_ball(self):
        app = BouncingBallSimulation(self.root)
        self.assertIsNotNone(app.ball)

    def test_bounce(self):
        app = BouncingBallSimulation(self.root)
        initial_max_height = app.max_height

        app.bounce()

        self.assertNotEqual(initial_max_height, app.max_height)

    def test_about_message(self):
        app = BouncingBallSimulation(self.root, main_about="Test About Message")
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            app._BouncingBallSimulation__about()
            mock_showinfo.assert_called_once_with("About", "Test About Message")

    def test_help_message(self):
        app = BouncingBallSimulation(self.root, main_help="Test Help Message")
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            app._BouncingBallSimulation__help()
            mock_showinfo.assert_called_once_with("Help", "Test Help Message")

    def test_version_message(self):
        app = BouncingBallSimulation(self.root, main_version="Test Version Message")
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            app._BouncingBallSimulation__version()
            mock_showinfo.assert_called_once_with("Version", "Test Version Message")


if __name__ == '__main__':
    unittest.main()
