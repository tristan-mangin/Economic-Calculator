package Main;

import java.util.Scanner;

/**
 * This class handles the entire running of the program. It will take user input and call needed 
 * classes.
 */
public class Main {

    /**
     * Outputs valid prompts for the program and suggestions as to how to use them
     * 
     * @returns none
     */
    public static void help() {
        System.out.println("List of Valid Prompts: \n" + 
                            "\thelp \t-\tlist valid prompts \n" +
                            "\tabout \t-\tlearn more about the program and how it works \n" +
                            "\tquit \t-\tend the program \n");
    }
    public static void main(String[] args) {

        // Start of the program and introduction
        Scanner reader = new Scanner(System.in);
        String prompt;
        boolean running = true;
        System.out.println("Welcome to the Economic Calculator!");
        System.out.println("\nPlease enter a prompt. For a list of promps type \'help\'. For more info type \'about\'");

        /**
         * Main loop of the program that will prompt the user for queries
         */
        while (running) {
            System.out.print(">> ");
            prompt = reader.nextLine().toLowerCase().trim();

            if (prompt.equals("help")) { help(); }
            else if (prompt.equals("about")) {  }
            else if (prompt.equals("quit")) { 
                running = false;
                break; 
            }
            else { System.out.println("Sorry that is an unknown prompt and/or has not been implemented yet.\n"); }
        }
    }
}
