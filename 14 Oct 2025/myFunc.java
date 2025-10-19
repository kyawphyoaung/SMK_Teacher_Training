import java.util.*;

public class myFunc {
    static String myName = "KPA";

    public static void hello(){
        System.out.println("Hello"+myName);
    }
    public static int dice(){
        Random rand = new Random();
        System.out.println(myName + "is rolling the dice");
        return 1+rand.nextInt(6);
    }
    public static void main(String[] args) {
        String email = "abc@gmail.com";
        hello();
        int number = dice();
        System.out.println(number);
    }

}