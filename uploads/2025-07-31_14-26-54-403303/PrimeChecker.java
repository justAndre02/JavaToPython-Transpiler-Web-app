public class PrimeChecker {
    public static void main(String[] args) {
        PrimeChecker checker = new PrimeChecker();
        int[] numbers = {2, 4, 5, 9, 13, 17, 20};

        for (int num : numbers) {
            if (checker.isPrime(num)) {
                System.out.println(num + " é primo.");
            } else {
                System.out.println(num + " não é primo.");
            }
        }
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
