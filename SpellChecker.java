import java.util.Scanner;
public class SpellChecker{
    public static void printArray(String []corrections){
        for (int j = 0; j < corrections.length; j++){
            System.out.print(corrections[j]+" ");
        }
        System.out.println("");
    }
    public static void main(String []args){
        Words wordDictionary = new Words("english.txt");

        Scanner inputReader = new Scanner(System.in);
        String sentence = inputReader.nextLine();

        String []wordList = sentence.split(" ");
        for (int i = 0; i < wordList.length; i++){
            if (!wordDictionary.isWord(wordList[i])){
                System.out.println("Correcting word " + wordList[i]);
                String []corrections = wordDictionary.getReplaceCorrections(wordList[i]);
                System.out.print("Replace corrections: ");
                printArray(corrections);
                corrections = wordDictionary.getDeleteCorrections(wordList[i]);
                System.out.print("Delete corrections: ");
                printArray(corrections);
                corrections = wordDictionary.getAddCorrections(wordList[i]);
                System.out.print("Add corrections: ");
                printArray(corrections);
            }
        }

    }
}