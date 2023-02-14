class Task(object):
    """
    Класс реализующий хранение атрибутов задачи.

    Атрибуты:

    * title: заголовок - string
    * manager_id: id создателя int
    * performers_id: id исполнителей int[]
    * deadline: дедлайн выполнения datetime
    * description: описание string[]

    """
    def __init__(self, info):
        """
        Принимает список параметров и присваивает их полям
        :param info: список параметров
        """
        # info = [title, manager_id, performers_id, deadline, description]
        self.title = info[0]
        self.manager_id = info[1]
        self.performers_id = info[2]
        self.deadline = info[3]
        self.description = info[4]

    def __str__(self):
        """
        Отображает содержимое в строку
        :return: строка, представляющая экземпляр
        """
        return f"Task(title=\"{self.title}\", " \
               f"manager_id={self.manager_id}, " \
               f"performers_id={self.performers_id}, " \
               f"deadline={self.deadline}, " \
               f"description={self.description})"
