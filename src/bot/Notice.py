class Notice(object):
    """
    Атрибуты:
    """
    def __init__(self, info):
        """
        Принимает список параметров и присваивает их полям
        :param info: список параметров
        info = [заголовок, id уведомляемых, время уведомления, описание]
        """
        self.title = info[0]
        self.recipients_id = info[1]
        self.deadline = info[2]
        self.description = info[3]

    def __str__(self):
        """
        Отображает содержимое в строку
        :return: строка, представляющая экземпляр
        """
        return f"Notice(title=\"{self.title}\", " \
               f"recipients_id={self.recipients_id}, " \
               f"deadline={self.deadline}, " \
               f"description={self.description})"

    def message(self):
        """
        Формирует текст уведомления
        :return: строка текста уведомления
        """
        mes = ''
        for recipient in self.recipients_id:
            mes += f'@{recipient}, '
        mes = mes[:-2] + '\n'
        mes += self.title + '\n'
        mes += self.description

        return mes
