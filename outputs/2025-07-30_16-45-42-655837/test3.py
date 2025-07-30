# Unit test result: ❌ FAILED (see log for details)
from enum import Enum, auto

class test3:

    class Priority(Enum):
        BAIXA = auto()
        MEDIA = auto()
        ALTA = auto()

    class Task:
        descricao: str
        prioridade: 'test3.Priority'

        def __init__(self, descricao: str, prioridade: 'test3.Priority'):
            self.descricao = descricao
            self.prioridade = prioridade

        def __str__(self) -> str:
            return f'[{self.prioridade.name}] {self.descricao}'

    @staticmethod
    def main(args: list[str]):
        tarefas: list['test3.Task'] = []
        continuar: bool = True
        while continuar:
            print('\n1. Adicionar tarefa')
            print('2. Listar tarefas')
            print('3. Sair')
            choice_str = input('Escolha uma opção: ')
            try:
                opcao = int(choice_str)
            except ValueError:
                print('Opção inválida. Por favor, insira um número.')
                continue
            match opcao:
                case 1:
                    desc = input('Descrição da tarefa: ')
                    prio_input = input('Prioridade (BAIXA, MEDIA, ALTA): ').upper()
                    prio: 'test3.Priority'
                    try:
                        prio = test3.Priority[prio_input]
                    except KeyError:
                        print('Prioridade inválida. Tarefa ignorada.')
                        continue
                    tarefas.append(test3.Task(desc, prio))
                    print('Tarefa adicionada.')
                case 2:
                    if not tarefas:
                        print('Nenhuma tarefa.')
                    else:
                        print('\nTarefas:')
                        for t in tarefas:
                            print(f'- {t}')
                case 3:
                    continuar = False
                    print('A sair...')
                case _:
                    print('Opção inválida.')
if __name__ == '__main__':
    test3.main([])