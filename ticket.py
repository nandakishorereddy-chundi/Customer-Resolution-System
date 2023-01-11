from enum import Enum

class Status(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    RESOLVED = 3
    BLOCKED = 4

class Ticket:
    def __init__(self):
        self.id = None
        self.issue_id = None
        self.agent_id = None
        self.status = None
        self.description = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_issue_id(self, issue_id):
        self.issue_id = issue_id

    def get_issue_id(self):
        return self.issue_id

    def set_agent_id(self, agent_id):
        self.agent_id = agent_id

    def get_agent_id(self):
        return self.agent_id

    def set_status(self, status):
        self.status = Status[status].name

    def get_status(self):
        return self.status

    def set_resolution(self, resolution):
        self.resolution = resolution

    def get_description(self):
        return self.resolution