# Unit test result: ✅ PASSED
import math

class PrimeChecker(object):

    @staticmethod
    def main(args: list[str]):
        checker = PrimeChecker()
        numbers = [2, 4, 5, 9, 13, 17, 20]
        for num in numbers:
            if checker.is_prime(num):
                print(f'{num} é primo.')
            else:
                print(f'{num} não é primo.')

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
if __name__ == '__main__':
    PrimeChecker.main([])