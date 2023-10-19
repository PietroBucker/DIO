import interfaces.AparelhoTelefonico;
import interfaces.NavegadorInternet;
import interfaces.ReprodutorMusical;

public abstract class SmartPhone implements AparelhoTelefonico, NavegadorInternet, ReprodutorMusical {
    protected String marca;


    public SmartPhone(String marca) {
        this.marca = marca;
    }

    @Override
    public void tocar() {
        
        System.out.println(this.marca + " esta Tocando");
    }

    @Override
    public void pausar() {
        
        System.out.println(this.marca + " estaPausado");
    }

    @Override
    public void selecionarMusica() {
        
        System.out.println(this.marca + " estaTrocando a Musica");
    }

    @Override
    public void exibirPagina() {
        
        System.out.println(this.marca + " esta abrindo pagina");
    }

    @Override
    public void adicionarNovaAba() {
        
        System.out.println(this.marca + " esta adicionando nova aba");
    }

    @Override
    public void atualizarPagina() {
        
        System.out.println(this.marca + " esta atualizando a pagina");
    }

    @Override
    public void ligar() {
        
        System.out.println(this.marca + " esta iniciando a chamada");
    }

    @Override
    public void atender() {
        
        System.out.println(this.marca + " atendeu a chamada ");
    }

    @Override
    public void iniciarCorrerioVoz() {
        
        System.out.println(this.marca + " esta direcionando para correio de voz");
    }
    
}
