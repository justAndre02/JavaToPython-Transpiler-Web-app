package test_files.test5;
import java.util.List;

public class test5 {
    public static Result processNumbers(List<Integer> numbers) {
        int sumEven = 0;
        int maxNumber = numbers.get(0);

        for (int num : numbers) {
            if (num % 2 == 0) {
                sumEven += num;
            }
            if (num > maxNumber) {
                maxNumber = num;
            }
        }

        return new Result(sumEven, maxNumber);
    }
}

class Result {
    public int sumEven;
    public int maxNumber;

    public Result(int sumEven, int maxNumber) {
        this.sumEven = sumEven;
        this.maxNumber = maxNumber;
    }
}