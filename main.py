from controller.main_controller import MainController
from tkinter import Tk

root = Tk()
root.title("Bouncing Ball Simulation")

controller = MainController()
app = controller.create(root)
controller.start_app(root)
