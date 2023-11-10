
from tkinter import Canvas, Menu, messagebox


class BouncingBallSimulation:
    def __init__(self, roottk, main_about="", main_version="", main_help="", width=800, height=600, ball_radius=100,
                 initial_height=100, restitution_coefficient=0.6, plane_height=50):
        self.root = roottk
        self.width = width
        self.height = height
        self.ball_radius = ball_radius
        self.restitution_coefficient = restitution_coefficient
        self.plane_height = plane_height
        self.flag = False

        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()

        self.ball = None
        self.max_height = initial_height
        self.create_ball()

        self.green_rectangle = self.canvas.create_rectangle(0, height - plane_height, width, height, fill="dark green")

        self.root.bind("<Escape>", self.exit_program)

        # меню
        self.__about_message = main_about
        self.__version_message = main_version
        self.__help_message = main_help
        self.__main_menu = Menu(self.root)
        self.__main_menu.add_command(label="About", command=self.__about)
        self.__main_menu.add_command(label="Help", command=self.__help)
        self.__main_menu.add_command(label="Version", command=self.__version)

        self.root.config(menu=self.__main_menu)

        self.run_simulation()

    def __about(self):
        """Отображает информационное окно "О программе"."""

        messagebox.showinfo("About", self.__about_message)

    def __help(self):
        """Отображает окно с информацией о использовании приложения."""

        messagebox.showinfo("Help", self.__help_message)

    def __version(self):
        """Отображает окно с информацией о версии приложения."""

        messagebox.showinfo("Version", self.__version_message)

    def create_ball(self):
        x = (self.width - self.ball_radius) // 2
        y = self.max_height - self.ball_radius
        self.ball = self.canvas.create_oval(x, y, x + self.ball_radius, y + self.ball_radius, fill="blue")

    def exit_program(self, event):
        self.root.destroy()

    def run_simulation(self):
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

