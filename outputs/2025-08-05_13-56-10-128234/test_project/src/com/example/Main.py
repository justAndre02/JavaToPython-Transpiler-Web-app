# Unit test result: ✅ PASSED
from com.example.model.User import User
from com.example.service.UserService import UserService
from typing import Optional

class Main:

    @staticmethod
    def main(args: list[str]):
        print('Starting User Management System...')
        service = UserService()
        service.create_user('Alice', 'alice@example.com')
        service.create_user('Bob', 'bob@example.com')
        service.print_all_users()
        print('\nSearching for user with ID 1...')
        found_user = service.find_user_by_id(1)
        if found_user is not None:
            print(f'Found: {found_user.get_name()}')
        else:
            print('User with ID 1 not found.')
        print('\nSystem finished.')
if __name__ == '__main__':
    Main.main([])