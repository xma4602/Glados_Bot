class Task:
    """
    Класс реализующий хранение атрибутов задачи.

    Атрибуты:

    * title: заголовок - string
    * manager_id: id создателя int
    * performers_id: id исполнителей int[]
    * deadline: дедлайн выполнения datetime
    * description: описание string[]

    """

    def __init__(self, task_data):
        """
        Принимает список параметров и присваивает их полям
        :param task_data: список параметров
        """
        # task_data = {title, manager_id, performers_id, deadline, description}
        self.title = task_data['title']
        self.manager_id = task_data['manager_id']
        self.performers_id = task_data['performers_id']
        self.deadline = task_data['deadline']
        self.description = task_data['description']

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
