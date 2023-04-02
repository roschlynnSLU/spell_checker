import java.util.Scanner;
public class SpellChecker{
    public static void main(String []args){
        Words wordDictionary = new Words("english.txt");

        Scanner inputReader = new Scanner(System.in);
        String sentence = inputReader.nextLine();

        String []wordList = sentence.split(" ");
        for (int i = 0; i < wordList.length; i++){
            if (!wordDictionary.isWord(wordList[i])){
                System.out.println("Correcting word " + wordList[i]);
            }
        }
    }
}