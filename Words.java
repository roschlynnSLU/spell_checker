import java.util.Scanner;
import java.util.HashMap;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class Words{
    private HashMap<String, Boolean> words;
    public Words(String fileName){
        words = new HashMap<String, Boolean>();
        String line = "";
        try{
            Scanner scanner = new Scanner(new FileInputStream(new File(fileName)));
            while (scanner.hasNextLine()){
                line = scanner.nextLine();
                words.put(line, true);
            }
        }
        catch (IOException error){
            System.out.println("Failed to construct Words " + error.getMessage());
        }
    }

    public boolean isWord(String word){
        boolean result = true;
        if (words.get(word) == null){
            result = false;
        }
        return result;
    }

    public int getSize(){
        return words.size();
    }
}