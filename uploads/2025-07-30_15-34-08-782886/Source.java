import javax.persistence.*;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import java.util.*;

@Entity
@Table(name = "produtos")
class Produto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nome;

    private Double preco;

    public Produto() {}

    public Produto(String nome, Double preco) {
        this.nome = nome;
        this.preco = preco;
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

    public Double getPreco() {
        return preco;
    }

    public void setPreco(Double preco) {
        this.preco = preco;
    }
}

public class HibernateDemo {

    private static SessionFactory factory;

    public static void main(String[] args) {

        try {
            factory = new Configuration()
                    .configure("hibernate.cfg.xml")
                    .addAnnotatedClass(Produto.class)
                    .buildSessionFactory();

            Session session = factory.getCurrentSession();

            Produto produto = new Produto("Teclado", 49.99);

            session.beginTransaction();
            session.save(produto);
            session.getTransaction().commit();

            session = factory.getCurrentSession();
            session.beginTransaction();
            Produto p = session.get(Produto.class, produto.getId());
            p.setPreco(39.99);
            session.getTransaction().commit();

            session = factory.getCurrentSession();
            session.beginTransaction();
            List<Produto> produtos = session.createQuery("from Produto", Produto.class).getResultList();
            for (Produto prod : produtos) {
                System.out.println(prod.getNome() + " - " + prod.getPreco());
            }
            session.getTransaction().commit();

            session = factory.getCurrentSession();
            session.beginTransaction();
            Produto toDelete = session.get(Produto.class, produto.getId());
            if (toDelete != null) {
                session.delete(toDelete);
            }
            session.getTransaction().commit();

        } finally {
            factory.close();
        }
    }
}
