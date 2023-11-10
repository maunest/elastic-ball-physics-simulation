from tkinter import Canvas, Menu, messagebox

class BouncingBallSimulation:
    """
    Класс BouncingBallSimulation представляет собой приложение для симуляции отскакивающего мяча.

    Параметры:
        - roottk: корневое окно Tkinter.
        - main_about: информация "About" для меню (по умолчанию пусто).
        - main_version: информация "Version" для меню (по умолчанию пусто).
        - main_help: информация "Help" для меню (по умолчанию пусто).
        - width: ширина окна (по умолчанию 800).
        - height: высота окна (по умолчанию 600).
        - ball_radius: радиус мяча (по умолчанию 100).
        - initial_height: начальная высота мяча (по умолчанию 100).
        - restitution_coefficient: коэффициент упругости мяча (по умолчанию 0.6).
        - plane_height: высота зоны отскока мяча (по умолчанию 50).
    """

    def __init__(self, roottk, main_about="", main_version="", main_help="", width=800, height=600, ball_radius=100,
                 initial_height=100, restitution_coefficient=0.6, plane_height=50):
        """
        Инициализация экземпляра класса BouncingBallSimulation.

        Создает главное окно приложения, настраивает его размер и размещает по центру экрана.
        Инициализирует элементы графического интерфейса, включая мяч, зону отскока и меню.

        Параметры:
            - roottk: корневое окно Tkinter.
            - main_about: информация "About" для меню (по умолчанию пусто).
            - main_version: информация "Version" для меню (по умолчанию пусто).
            - main_help: информация "Help" для меню (по умолчанию пусто).
            - width: ширина окна (по умолчанию 800).
            - height: высота окна (по умолчанию 600).
            - ball_radius: радиус мяча (по умолчанию 100).
            - initial_height: начальная высота мяча (по умолчанию 100).
            - restitution_coefficient: коэффициент упругости мяча (по умолчанию 0.6).
            - plane_height: высота нижней платформы (по умолчанию 50).
        """

        # Инициализация основных параметров
        self.root = roottk
        self.width = width
        self.height = height
        self.ball_radius = ball_radius
        self.restitution_coefficient = restitution_coefficient
        self.plane_height = plane_height
        self.flag = False

        # Получаем размеры экрана
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Вычисляем координаты для центрирования окна
        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2

        # Устанавливаем размер и положение окна
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")

        # Создаем и настраиваем Canvas (холст) для отображения графики
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()

        # Инициализация переменных для мяча и высоты
        self.ball = None
        self.max_height = initial_height

        # Создание мяча и зоны отскока
        self.create_ball()
        self.green_rectangle = self.canvas.create_rectangle(0, height - plane_height, width, height, fill="dark green")

        # Привязка события "Escape" к методу завершения программы
        self.root.bind("<Escape>", self.exit_program)

        # Создание меню
        self.__about_message = main_about
        self.__version_message = main_version
        self.__help_message = main_help
        self.__main_menu = Menu(self.root)
        self.__main_menu.add_command(label="About", command=self.__about)
        self.__main_menu.add_command(label="Help", command=self.__help)
        self.__main_menu.add_command(label="Version", command=self.__version)

        # Установка меню в корневое окно
        self.root.config(menu=self.__main_menu)

        # Запуск основной симуляции
        self.run_simulation()

    def __about(self):
        """
        Отображает информационное окно "О программе".
        """
        messagebox.showinfo("About", self.__about_message)

    def __help(self):
        """
        Отображает окно с информацией о использовании приложения.
        """
        messagebox.showinfo("Help", self.__help_message)

    def __version(self):
        """
        Отображает окно с информацией о версии приложения.
        """
        messagebox.showinfo("Version", self.__version_message)

    def create_ball(self):
        """
        Создает мяч на холсте.
        """
        x = (self.width - self.ball_radius) // 2
        y = self.max_height - self.ball_radius
        self.ball = self.canvas.create_oval(x, y, x + self.ball_radius, y + self.ball_radius, fill="blue")

    def exit_program(self, event):
        """
        Обработчик события "Escape". Завершает программу.
        """
        self.root.destroy()

    def run_simulation(self):
        """
        Запускает основной цикл симуляции, обновляя положение мяча на холсте.
        """
        while True:
            ball_coords = self.canvas.coords(self.ball)
            ball_center_y = ball_coords[1] + self.ball_radius

            if ball_center_y >= self.height - self.plane_height:
                self.bounce()
                if self.flag:
                    break

            self.canvas.move(self.ball, 0, 7)
            self.root.update()
            self.root.after(30)

    def bounce(self):
        """
        Обрабатывает отскок мяча от зоны отскока.
        """
        self.max_height = (self.height - self.plane_height) - (
                    self.height - self.plane_height - self.max_height) * self.restitution_coefficient

        if self.height < self.max_height + self.plane_height + self.ball_radius / 20:
            self.flag = True
            self.canvas.move(self.ball, 0, -self.ball_radius / 20)
        else:
            while True:
                ball_coords = self.canvas.coords(self.ball)
                ball_center_y = ball_coords[1] + self.ball_radius

                if ball_center_y <= self.max_height:
                    break

                self.canvas.move(self.ball, 0, -7)
                self.root.update()
                self.root.after(30)
