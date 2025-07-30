# Unit test result: ✅ PASSED
from typing import Optional
from com.example.model.User import User
from com.example.service.UserService import UserService

class Main:

    @staticmethod
    def main(args: list[str]) -> None:
        print('Starting User Management System...')
        service: UserService = UserService()
        service.createUser('Alice', 'alice@example.com')
        service.createUser('Bob', 'bob@example.com')
        service.printAllUsers()
        print('\nSearching for user with ID 1...')
        found_user: Optional[User] = service.findUserById(1)
        if found_user is not None:
            print(f'Found: {found_user.getName()}')
        else:
            print('User with ID 1 not found.')
        print('\nSystem finished.')
if __name__ == '__main__':
    Main.main([])