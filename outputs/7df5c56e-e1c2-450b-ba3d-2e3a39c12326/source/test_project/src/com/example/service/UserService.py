# Unit test result: ✅ PASSED
from typing import Optional
from com.example.model.User import User

class UserService:
    userDatabase: list['User']
    nextId: int = 1

    def __init__(self):
        self.userDatabase = []

    def create_user(self, name: str, email: str) -> 'User':
        new_user = User(self.nextId, name, email)
        self.nextId += 1
        self.userDatabase.append(new_user)
        print(f'Created new user: {new_user.get_name()}')
        return new_user

    def find_user_by_id(self, id: int) -> Optional['User']:
        for user in self.userDatabase:
            if user.get_id() == id:
                return user
        return None

    def print_all_users(self) -> None:
        print('--- All Users ---')
        if not self.userDatabase:
            print('No users in the database.')
        else:
            for user in self.userDatabase:
                print(str(user))
        print('-----------------')