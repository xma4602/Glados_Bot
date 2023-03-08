from datetime import datetime


class Notice(object):
    """
    Атрибуты:
    """

    def __init__(self, notice_data: dict):
        """
        Принимает список параметров и присваивает их полям
        :param notice_data: список параметров
        """
        self.title = notice_data[0]
        self.recipients_id = notice_data[1]
        self.time = notice_data[2]
        self.description = notice_data[3]

    def __init__(self, title: str, recipients_id: list, time: datetime, description: list):
        self.title = title
        self.recipients_id = recipients_id
        self.time = time
        self.description = description

    def __str__(self):
        """
        Отображает содержимое в строку
        :return: строка, представляющая экземпляр
        """
        return f"Notice(title=\"{self.title}\", " \
               f"recipients_id={self.recipients_id}, " \
               f"deadline={self.time}, " \
               f"description={self.description})"

    def message_everyone(self):
        """
        Формирует текст уведомления для всех получателей
        :return: строка текста уведомления
        """
        mes = ''
        for recipient in self.recipients_id:
            mes += f'@{recipient}, '
        # удаление лишней пунктуации
        mes = mes[:-2] + '\n'
        mes += self.title + '\n'
        mes += self.description

        return mes
