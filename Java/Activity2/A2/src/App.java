import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        double num1, num2, answer;

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println(name + ", add two numbers.");

        System.out.print("Enter first number: ");
        num1 = scanner.nextDouble();
        System.out.print("Enter second number: ");
        num2 = scanner.nextDouble();
        answer = num1 + num2;
        System.out.println(name + ", the sum is " + answer);

        
    }
}
