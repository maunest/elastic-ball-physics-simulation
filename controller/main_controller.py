from storage.storage import Storage
from app.bouncing_ball_simulation import BouncingBallSimulation


class MainController:
    """
    Класс MainController отвечает за управление созданием и запуском главного окна приложения.

    Методы:
        - create(root): Создает экземпляр BouncingBallSimulation, используя информацию из хранилища.
        - start_app(root): Запускает главный цикл обработки событий Tkinter.

    Параметры:
        - root: корневое окно Tkinter.
    """

    @staticmethod
    def create(root):
        """
        Создает экземпляр BouncingBallSimulation, используя информацию из хранилища.

        Параметры:
            - root: корневое окно Tkinter.
        """
        storage = Storage()

        # Получение информации "About", "Version" и "Help" из хранилища
        main_about = storage.get_about()
        main_version = storage.get_version()
        main_help = storage.get_help()

        # Создание экземпляра BouncingBallSimulation с передачей информации из хранилища
        BouncingBallSimulation(root, main_about, main_version, main_help)

    @staticmethod
    def start_app(root):
        """
        Запускает главный цикл обработки событий Tkinter.

        Параметры:
            - root: корневое окно Tkinter.
        """
        root.mainloop()
