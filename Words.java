import java.util.Scanner;
import java.util.HashSet;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;

public class Words{
    private HashSet<String> words;
    public Words(String fileName){
        words = new HashSet<String>();
        String line = "";
        try{
            Scanner scanner = new Scanner(new FileInputStream(new File(fileName)));
            while (scanner.hasNextLine()){
                line = scanner.nextLine();
                words.add(line);
            }
        }
        catch (IOException error){
            System.out.println("Failed to construct Words " + error.getMessage());
        }
    }

    public boolean isWord(String word){
        boolean result = true;
        if (!words.contains(word)) {
            result = false;
        }
        return result;
    }

    public int getSize(){
        return words.size();
    }

    public String[] getReplaceCorrections(String misspelledWord){
        ArrayList<String> suggestions = new ArrayList<String>();
        for (String word: this.words){
            if (word.length() == misspelledWord.length()){
                for (int i = 0; i < misspelledWord.length(); i++){
                    String correction = misspelledWord.substring(0, i)+word.charAt(i);
                    if ( i < misspelledWord.length() - 1){
                        correction+=misspelledWord.substring(i+1);
                    }
                    if (correction.equals(word)){
                        suggestions.add(correction);
                        break;
                    }
                }

            }
        }
        return arrayListToArray(suggestions);
    }

    public String[] getDeleteCorrections(String misspelledWord){
        ArrayList<String> suggestions = new ArrayList<String>();
        for (String word: this.words){
            if (word.length() == misspelledWord.length()-1){
                if (canTransformWithDelete(misspelledWord, word)){
                    suggestions.add(word);
                }
            }
        }
        return arrayListToArray(suggestions);
    }

    public String[] getAddCorrections(String misspelledWord){
        ArrayList<String> suggestions = new ArrayList<String>();
        for (String word: this.words){
            if (word.length() == misspelledWord.length()+1){
                if (canTransformWithDelete(word, misspelledWord)){
                    suggestions.add(word);
                }
            }
        }
        return arrayListToArray(suggestions);
    }

    private boolean canTransformWithDelete(String from, String to){
        boolean transformed = false;
        for (int i = 0; i < from.length(); i++){
            String correction = from.substring(0, i);
            if ( i < from.length() - 1){
                correction+=from.substring(i+1);
            }
            if (correction.equals(to)){
                transformed = true;
                break;
            }
        }
        return transformed;
    }

    private String[] arrayListToArray(ArrayList<String> suggestions){
        String []result = new String[suggestions.size()];
        int index = 0;
        for (String w: suggestions){
            result[index] = w;
            index++;
        }
        return result;
    }
}