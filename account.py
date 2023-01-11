class Account:
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email