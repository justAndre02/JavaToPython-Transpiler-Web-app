# Unit test result: ✅ PASSED
class test5:

    @staticmethod
    def process_numbers(numbers: list[int]) -> 'Result':
        sum_even: int = 0
        max_number: int = numbers[0]
        for num in numbers:
            if num % 2 == 0:
                sum_even += num
            if num > max_number:
                max_number = num
        return Result(sum_even, max_number)

class Result:
    sumEven: int
    maxNumber: int

    def __init__(self, sumEven: int, maxNumber: int):
        self.sumEven = sumEven
        self.maxNumber = maxNumber