import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args){
        String[] students ={"Mg Mg","Aye Aye","Kyaw Kyaw"};
        try{
            FileWriter myFile = new FileWriter("student_list.txt");
            for(int i=0; i < students.length; i++){
                myFile.write(students[i]+",");
            }
            myFile.close();
        }catch(IOException e){
            System.out.println("Error:"+e);
        }
    }

}