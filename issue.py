from enum import Enum

class IssueType(Enum):
    PAYMENT = 1
    MUTAL_FUND = 2
    GOLD = 3
    INSURANCE = 4


class Issue:
    def __init__(self):
        self.id = None
        self.transaction_id = None
        self.user_email = None
        self.issue_type = None
        self.subject = None
        self.description = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    def get_transaction_id(self):
        return self.transaction_id

    def set_user_email(self, email):
        self.user_email = email

    def get_user_email(self):
        return self.user_email

    def set_issue_type(self, issue_type):
        self.issue_type = IssueType[issue_type].name

    def get_issue_type(self):
        return self.issue_type

    def set_subject(self, subject):
        self.subject = subject

    def get_subject(self):
        return self.subject

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
