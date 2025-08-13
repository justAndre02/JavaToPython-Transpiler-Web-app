interface Operacao {
    int aplicar(int a, int b);
}

class Soma implements Operacao {
    public int aplicar(int a, int b) {
        return a + b;
    }
}

class TesteInterface {
    public static void main(String[] args) {
        Operacao op = new Soma();
        System.out.println(op.aplicar(3, 4)); // 7
    }
}
