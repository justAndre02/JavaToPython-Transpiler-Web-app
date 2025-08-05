# Unit test result: ❌ FAILED (see log for details)
from com.example.model.User import User
from typing import Optional

class UserService:
    user_database: list['User']
    next_id: int = 1

    def __init__(self):
        self.user_database = []

    def create_user(self, name: str, email: str) -> 'User':
        new_user = User(self.next_id, name, email)
        self.next_id += 1
        self.user_database(new_user)
        print(f'Created new user: {new_user.get_name()}')
        return new_user

    def find_user_by_id(self, id: int) -> Optional['User']:
        for user in self.user_database:
            if user.get_id() == id:
                return user
        return None

    def print_all_users(self) -> None:
        print('--- All Users ---')
        if not self.user_database:
            print('No users in the database.')
        else:
            for user in self.user_database:
                print(str(user))
        print('-----------------')