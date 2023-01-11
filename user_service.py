from user import User

class UserService:
    users = {}

    def create_user(self, id, name, email):
         user = User()
         user.set_id(id)
         user.set_name(name)
         user.set_email(email)
         users[id] = user
         return user