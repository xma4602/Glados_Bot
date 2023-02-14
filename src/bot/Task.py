class Task(object):
    def __init__(self, info):
        # info = [title, manager_id, performers_id, deadline, description]
        self.title = info[0]
        self.manager_id = info[1]
        self.performers_id = info[2]
        self.deadline = info[3]
        self.description = info[4]

    def __str__(self):
        return f"Task(title=\"{self.title}\", " \
               f"manager_id={self.manager_id}, " \
               f"performers_id={self.performers_id}, " \
               f"deadline={self.deadline}, " \
               f"description={self.description})"
