# Unit test result: ✅ PASSED
class test2:

    @staticmethod
    def main(args: list[str]):
        a = 5
        b = 7
        print(f'Soma: {test2.add(a, b)}')

    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y
if __name__ == '__main__':
    test2.main([])