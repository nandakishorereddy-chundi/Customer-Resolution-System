from account import Account

class Agent(Account):
    def __init__(self):
        super().__init__()
        self.specializations = []
        self.issues = []

    def set_specializations(self, specializations):
        self.specializations = specializations

    def get_specializations(self):
        return self.specializations

    def add_issue(self, issue):
        self.issues.append(issue)
    
    def get_issues(self):
        return self.issues