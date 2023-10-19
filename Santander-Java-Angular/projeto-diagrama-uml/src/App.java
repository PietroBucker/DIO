public class App {
    public static void main(String[] args) throws Exception {
        Iphone iphone = new Iphone("iphone 8");
        iphone.atender();
        iphone.ligar();
        iphone.iniciarCorrerioVoz();
        iphone.tocar();
        iphone.pausar();
        iphone.selecionarMusica();
        iphone.exibirPagina();
        iphone.adicionarNovaAba();
        iphone.atualizarPagina();
    }
}
