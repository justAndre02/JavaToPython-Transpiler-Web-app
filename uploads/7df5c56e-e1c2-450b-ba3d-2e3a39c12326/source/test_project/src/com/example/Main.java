package com.example;

import com.example.model.User;
import com.example.service.UserService;

public class Main {
    public static void main(String[] args) {
        System.out.println("Starting User Management System...");

        UserService service = new UserService();

        // Create some users
        service.createUser("Alice", "alice@example.com");
        service.createUser("Bob", "bob@example.com");

        // Print all users
        service.printAllUsers();

        // Find a specific user
        System.out.println("\nSearching for user with ID 1...");
        User foundUser = service.findUserById(1);
        if (foundUser != null) {
            System.out.println("Found: " + foundUser.getName());
        } else {
            System.out.println("User with ID 1 not found.");
        }
        
        System.out.println("\nSystem finished.");
    }
}