
class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def create_my_user(self, username, password):
        return self.user_dao.create_user(username, password)



