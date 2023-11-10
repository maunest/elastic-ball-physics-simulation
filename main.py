from controller.main_controller import MainController
from tkinter import Tk

# Создание корневого (главного) окна приложения
root = Tk()
root.title("Bouncing Ball Simulation")  # Установка заголовка окна

# Создание экземпляра главного контроллера
controller = MainController()

# Создание и инициализация графического интерфейса приложения
app = controller.create(root)

# Запуск основной логики приложения через контроллер
controller.start_app(root)