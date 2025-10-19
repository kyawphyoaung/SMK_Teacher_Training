import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args){
        try{
            FileWriter myFile = new FileWriter("app.txt");
            myFile.write("Student 1\n");
            myFile.write("Student 2\n");
            myFile.write("Student 3\n");
            myFile.close();
        } catch (IOException e){
            System.out.println("Error:"+e);
        }
    }

}