import datetime

club_council_path = r'src/club_council.txt'




# noinspection PyGlobalUndefined
class Task(object):
    def __init__(self, info):
        # info = [title, manager_id, performers_id, deadline, description]
        self.title = info[0]
        self.manager_id = Task.get_user_id(info[1])
        self.performers_id = Task.get_performers_id(info[2])
        self.deadline = Task.get_deadline(info[3])
        self.description = info[4]

    def __str__(self):
        return f"Task(title=\"{self.title}\", " \
               f"manager_id={self.manager_id}, " \
               f"performers_id={self.performers_id}, " \
               f"deadline={self.deadline}, " \
               f"description=\"{self.description}\")"

    @staticmethod
    def get_user_id(user_name):
        global id
        user_name = user_name.lower()
        file = open(club_council_path, 'r', encoding="utf-8")

        try:
            name, id = file.readline().split(' ')
            while name != user_name:
                name, id = file.readline().split(' ')
        finally:
            file.close()
            return id

    @staticmethod
    def get_performers_id(users_names):
        global id
        for i in range(len(users_names)):
            users_names[i] = users_names[i].lower()
        file = open(club_council_path, 'r', encoding="utf-8")

        try:
            for i in range(len(users_names)):
                name, id = file.readline().replace('\n', '').split(' ')
                while name != users_names[i]:
                    name, id = file.readline().replace('\n', '').split(' ')

                if file.read() == '':
                    return -1
                else:
                    users_names[i] = id
                    file.seek(0)
        finally:
            file.close()
            return users_names

    @staticmethod
    def get_deadline(dates):
        global deadline
        for date in dates:
            if not date.isalpha():
                deadline = date
                break
        deadline = deadline.split('.')
        return datetime.date(
            day=int(deadline[0]),
            month=int(deadline[1]),
            year=datetime.datetime.today().year)
