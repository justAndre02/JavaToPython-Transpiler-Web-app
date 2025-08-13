# Unit test result: ✅ PASSED
from abc import ABC, abstractmethod

class Operacao(ABC):

    @abstractmethod
    def aplicar(self, a: int, b: int) -> int:
        pass

class Soma(Operacao):

    def aplicar(self, a: int, b: int) -> int:
        return a + b

class TesteInterface:

    @staticmethod
    def main(args: list[str]) -> None:
        op = Soma()
        print(op.aplicar(3, 4))
if __name__ == '__main__':
    TesteInterface.main([])