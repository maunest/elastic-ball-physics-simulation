from storage.storage import Storage
from app.bouncing_ball_simulation import BouncingBallSimulation


class MainController:

    @staticmethod
    def create(root):
        storage = Storage()
        main_about = storage.get_about()
        main_version = storage.get_version()
        main_help = storage.get_help()

        BouncingBallSimulation(root, main_about, main_version, main_help)

    @staticmethod
    def start_app(root):
        root.mainloop()
