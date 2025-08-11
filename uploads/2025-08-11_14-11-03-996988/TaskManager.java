import java.util.ArrayList;
import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class TaskManager {
    private ArrayList<Task> tasks;
    private Scanner scanner;
    
    public TaskManager() {
        tasks = new ArrayList<>();
        scanner = new Scanner(System.in);
    }
    
    public void addTask(String description, int priority) {
        Task newTask = new Task(description, priority);
        tasks.add(newTask);
        System.out.println("Task added successfully!");
    }
    
    public void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks available.");
            return;
        }
        
        System.out.println("\n===== TASK LIST =====");
        for (int i = 0; i < tasks.size(); i++) {
            Task task = tasks.get(i);
            String status = task.isCompleted() ? "[COMPLETED]" : "[PENDING]";
            System.out.printf("%d. %s - %s (Priority: %d) Created: %s\n", 
                i + 1, status, task.getDescription(), task.getPriority(), 
                task.getCreationDate());
        }
        System.out.println("=====================\n");
    }
    
    public void markTaskAsComplete(int taskIndex) {
        if (taskIndex >= 0 && taskIndex < tasks.size()) {
            Task task = tasks.get(taskIndex);
            task.setCompleted(true);
            System.out.println("Task marked as complete!");
        } else {
            System.out.println("Invalid task number.");
        }
    }
    
    public void run() {
        boolean running = true;
        
        System.out.println("Welcome to Task Manager!");
        
        while (running) {
            System.out.println("\nPlease select an option:");
            System.out.println("1. Add new task");
            System.out.println("2. View all tasks");
            System.out.println("3. Mark task as complete");
            System.out.println("4. Exit");
            System.out.print("Your choice: ");
            
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            
            switch (choice) {
                case 1:
                    System.out.print("Enter task description: ");
                    String description = scanner.nextLine();
                    System.out.print("Enter priority (1-5): ");
                    int priority = scanner.nextInt();
                    scanner.nextLine(); // Consume newline
                    addTask(description, priority);
                    break;
                case 2:
                    viewTasks();
                    break;
                case 3:
                    viewTasks();
                    System.out.print("Enter task number to mark as complete: ");
                    int taskNum = scanner.nextInt();
                    scanner.nextLine(); // Consume newline
                    markTaskAsComplete(taskNum - 1);
                    break;
                case 4:
                    running = false;
                    System.out.println("Thank you for using Task Manager!");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
        
        scanner.close();
    }
    
    public static void main(String[] args) {
        TaskManager manager = new TaskManager();
        manager.run();
    }
}

class Task {
    private String description;
    private boolean completed;
    private int priority;
    private String creationDate;
    
    public Task(String description, int priority) {
        this.description = description;
        this.completed = false;
        this.priority = priority;
        
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        this.creationDate = now.format(formatter);
    }
    
    public String getDescription() {
        return description;
    }
    
    public boolean isCompleted() {
        return completed;
    }
    
    public void setCompleted(boolean completed) {
        this.completed = completed;
    }
    
    public int getPriority() {
        return this.priority;
    }
    
    public String getCreationDate() {
        return creationDate;
    }
}