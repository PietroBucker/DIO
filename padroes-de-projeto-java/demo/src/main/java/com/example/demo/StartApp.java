package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.example.demo.model.Book;
import com.example.demo.repository.UserRepository;


@Component
public class StartApp implements CommandLineRunner {
    @Autowired
    private UserRepository repository;
    @Override
    public void run(String... args) throws Exception {
        Book book = new Book();
        book.setName("Primeiro Livro");
        book.setAuthor("Pietro");

        repository.save(book);

        for(Book u: repository.findAll()){
            System.out.println(u);
        }
    }
}
  