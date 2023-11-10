class Storage:
    """Класс Storage содержит текстовую информацию для заголовка.

    Attributes:
        __about (str): Информация о приложении.
        __version (str): Версия приложения.
        __help (str): Справочная информация.

    Methods:
        get_about() -> str: Возвращает информацию "О программе".
        get_version() -> str: Возвращает текущую версию приложения.
        get_help() -> str: Возвращает справочную информацию.
    """

    def __init__(self):
        """Инициализация объекта Storage с пустыми значениями.
        """

        with open('storage/data/about.txt', 'r') as file:
            self.__about = file.read()

        with open('storage/data/version.txt', 'r') as file:
            self.__version = file.read()

        with open('storage/data/help.txt', 'r') as file:
            self.__help = file.read()

    def get_about(self) -> str:
        """Возвращает информацию "О программе".

        Returns:
            str: Информация "О программе".
        """
        return self.__about

    def get_version(self) -> str:
        """Возвращает текущую версию приложения.

        Returns:
            str: Версия приложения.
        """
        return self.__version

    def get_help(self) -> str:
        """Возвращает справочную информацию.

        Returns:
            str: Справочная информация.
        """
        return self.__help
