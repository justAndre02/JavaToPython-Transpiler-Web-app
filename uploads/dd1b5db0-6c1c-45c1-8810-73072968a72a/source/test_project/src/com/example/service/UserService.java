package com.example.service;

import com.example.model.User;
import java.util.ArrayList;
import java.util.List;

public class UserService {
    private List<User> userDatabase;
    private int nextId = 1;

    public UserService() {
        this.userDatabase = new ArrayList<>();
    }

    public User createUser(String name, String email) {
        User newUser = new User(nextId++, name, email);
        userDatabase.add(newUser);
        System.out.println("Created new user: " + newUser.getName());
        return newUser;
    }

    public User findUserById(int id) {
        for (User user : userDatabase) {
            if (user.getId() == id) {
                return user;
            }
        }
        return null; // User not found
    }

    public void printAllUsers() {
        System.out.println("--- All Users ---");
        if (userDatabase.isEmpty()) {
            System.out.println("No users in the database.");
        } else {
            for (User user : userDatabase) {
                System.out.println(user.toString());
            }
        }
        System.out.println("-----------------");
    }
}