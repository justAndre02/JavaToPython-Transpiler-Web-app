package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Service;
import org.springframework.stereotype.Repository;
import org.springframework.beans.factory.annotation.Autowired;
import javax.annotation.PostConstruct;
import java.util.*;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    /**
     * Entidade simples para representar um Utilizador
     */
    public static class Usuario {
        private Long id;
        private String nome;
        private String email;

        public Usuario() {}

        public Usuario(Long id, String nome, String email) {
            this.id = id;
            this.nome = nome;
            this.email = email;
        }

        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public String getNome() {
            return nome;
        }

        public void setNome(String nome) {
            this.nome = nome;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }
    }

    /**
     * Controlador REST para gerir Utilizadores
     */
    @RestController
    @RequestMapping("/api/usuarios")
    public static class UsuarioController {

        @Autowired
        private UsuarioService service;

        @GetMapping
        public List<Usuario> listar() {
            return service.obterTodos();
        }

        @GetMapping("/{id}")
        public Usuario obter(@PathVariable Long id) {
            return service.obterPorId(id);
        }

        @PostMapping
        public Usuario criar(@RequestBody Usuario usuario) {
            return service.criar(usuario);
        }

        @PutMapping("/{id}")
        public Usuario atualizar(@PathVariable Long id, @RequestBody Usuario usuario) {
            usuario.setId(id);
            return service.atualizar(usuario);
        }

        @DeleteMapping("/{id}")
        public void remover(@PathVariable Long id) {
            service.remover(id);
        }
    }

    /**
     * Serviço de negócio para Utilizadores
     */
    @Service
    public static class UsuarioService {

        @Autowired
        private UsuarioRepository repo;

        public List<Usuario> obterTodos() {
            return repo.findAll();
        }

        public Usuario obterPorId(Long id) {
            return repo.findById(id).orElse(null);
        }

        public Usuario criar(Usuario usuario) {
            return repo.save(usuario);
        }

        public Usuario atualizar(Usuario usuario) {
            return repo.save(usuario);
        }

        public void remover(Long id) {
            repo.deleteById(id);
        }
    }

    /**
     * Repositório simulado em memória para Utilizadores
     */
    @Repository
    public static class UsuarioRepository {

        private Map<Long, Usuario> armazenamento = new HashMap<>();
        private Long sequence = 0L;

        @PostConstruct
        public void init() {
            // Preencher com alguns dados iniciais
            save(new Usuario(null, "Alice", "alice@example.com"));
            save(new Usuario(null, "Bruno", "bruno@example.com"));
        }

        public Optional<Usuario> findById(Long id) {
            return Optional.ofNullable(armazenamento.get(id));
        }

        public List<Usuario> findAll() {
            return new ArrayList<>(armazenamento.values());
        }

        public Usuario save(Usuario usuario) {
            if (usuario.getId() == null) {
                usuario.setId(++sequence);
            }
            armazenamento.put(usuario.getId(), usuario);
            return usuario;
        }

        public void deleteById(Long id) {
            armazenamento.remove(id);
        }
    }
}
