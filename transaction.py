from enum import Enum

class TransactionStatus(Enum):
    SUCCESS = 1
    FAILED = 2

class Transaction:

    def __init__(self):
        self.id = None
        self.user_id = None
        self.status = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_status(self, status):
        self.status = TransactionStatus[status].name

    def get_status(self):
        return self.status