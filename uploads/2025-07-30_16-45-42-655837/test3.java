package test_files.test3;
import java.util.ArrayList;
import java.util.Scanner;

public class test3 {

    enum Priority {
        BAIXA, MEDIA, ALTA
    }

    static class Task {
        String descricao;
        Priority prioridade;

        Task(String descricao, Priority prioridade) {
            this.descricao = descricao;
            this.prioridade = prioridade;
        }

        public String toString() {
            return "[" + prioridade + "] " + descricao;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Task> tarefas = new ArrayList<>();
        boolean continuar = true;

        while (continuar) {
            System.out.println("\n1. Adicionar tarefa");
            System.out.println("2. Listar tarefas");
            System.out.println("3. Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine(); // consumir newline

            switch (opcao) {
                case 1:
                    System.out.print("Descrição da tarefa: ");
                    String desc = scanner.nextLine();
                    System.out.print("Prioridade (BAIXA, MEDIA, ALTA): ");
                    String prioInput = scanner.nextLine().toUpperCase();
                    Priority prio;
                    try {
                        prio = Priority.valueOf(prioInput);
                    } catch (IllegalArgumentException e) {
                        System.out.println("Prioridade inválida. Tarefa ignorada.");
                        break;
                    }
                    tarefas.add(new Task(desc, prio));
                    System.out.println("Tarefa adicionada.");
                    break;
                case 2:
                    if (tarefas.isEmpty()) {
                        System.out.println("Nenhuma tarefa.");
                    } else {
                        System.out.println("\nTarefas:");
                        for (Task t : tarefas) {
                            System.out.println("- " + t);
                        }
                    }
                    break;
                case 3:
                    continuar = false;
                    System.out.println("A sair...");
                    break;
                default:
                    System.out.println("Opção inválida.");
            }
        }

        scanner.close();
    }
}
