public class ParametrosInvalidosException extends Exception {
    public String getMessage() {
        return "Primeiro numero deve ser menor que o segundo numero";
    }

    @Override
    public String toString() {
        return "ParametrosInvalidosException []";
    }
   
}
