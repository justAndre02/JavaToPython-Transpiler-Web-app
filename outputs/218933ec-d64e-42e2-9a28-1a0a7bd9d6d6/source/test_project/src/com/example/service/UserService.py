# Unit test result: ✅ PASSED
from com.example.model.User import User
from typing import Optional

class UserService:
    userDatabase: list['User']
    nextId: int = 1

    def __init__(self):
        self.userDatabase = []

    def createUser(self, name: str, email: str) -> 'User':
        new_user = User(self.nextId, name, email)
        self.nextId += 1
        self.userDatabase.append(new_user)
        print(f'Created new user: {new_user.getName()}')
        return new_user

    def findUserById(self, id: int) -> Optional['User']:
        for user in self.userDatabase:
            if user.getId() == id:
                return user
        return None

    def printAllUsers(self):
        print('--- All Users ---')
        if not self.userDatabase:
            print('No users in the database.')
        else:
            for user in self.userDatabase:
                print(str(user))
        print('-----------------')