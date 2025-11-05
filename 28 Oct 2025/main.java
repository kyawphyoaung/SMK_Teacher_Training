import java.util.*;
public class main{
    public static void newUser(){
        System.out.print("New User Registration Function");
    }
    public static void main(String[] args) {
        System.out.println("1. New User Registration");
        System.out.println("2. User Login");
        System.out.println("3. Forgot Password");
        System.out.println("4. Exit");
        Scanner sc = new Scanner(System.in);
        int choice = sc.nextInt();

        switch(choice){
            case 1:
                newUser();
            break;

            case 2:
                System.out.println("User Login Function");
            break;

            case 3:
                System.out.println("Forgot Password Function");
            break;

            case 4:
                System.out.println("Exit Function");
            break;

            default:
                System.out.println("Invalid option");
            break;
        }
        sc.close();
    }
}