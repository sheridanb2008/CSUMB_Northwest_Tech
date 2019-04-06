/*
 * Assignment: GUI Cards
 * Names:      Brian Sheridan, Craig Calvert, Kevin Bentley, Samuel Pearce
 * Course:     CST338 - Spring B
 * Date:       04/??/2019
 * Objective:
 */

import javax.swing.*;
import java.awt.*;

public class Assign5
{
   static final int NUM_CARD_IMAGES = 57; // 52 + 4 jokers + 1 back-of-card image
   static Icon[] icon = new ImageIcon[NUM_CARD_IMAGES];

   static void loadCardIcons()
   {
      String suit;
      String cardValue;
      int cardCount = 0;

      // Builds the file names ("AC.gif", "2C.gif", "3C.gif", "TC.gif", etc.)
      // and inserts them into the ImageIcon array.
      for (int suitCount = 0; suitCount < 4; suitCount++)
      {
         suit = turnIntIntoCardSuit(suitCount);

         for (int valueCount = 0; valueCount < 14; valueCount++)
         {
            cardValue = turnIntIntoCardValue(valueCount);
            icon[cardCount] = new ImageIcon(Assign5.class.getResource("images/" + cardValue + suit + ".gif"));
            cardCount++;
         }
      }

      // Adds the card-back image icon
      icon[cardCount] = new ImageIcon(Assign5.class.getResource("images/BK.gif"));
   }

   // turns 0 - 13 into "A", "2", "3", ... "Q", "K", "X"
   static String turnIntIntoCardValue(int k)
   {
      String[] cardValue = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T",
            "J", "Q", "K", "X"};
      return cardValue[k];
   }

   // turns 0 - 3 into "C", "D", "H", "S"
   static String turnIntIntoCardSuit(int j)
   {
      String[] suit = {"C", "D", "H", "S"};
      return suit[j];
   }

   // a simple main to throw all the JLabels out there for the world to see
   public static void main(String[] args)
   {
      int k;

      // prepare the image icon array
      loadCardIcons();

      // establish main frame in which program will run
      JFrame frmMyWindow = new JFrame("Card Room");
      frmMyWindow.setSize(1150, 650);
      frmMyWindow.setLocationRelativeTo(null);
      frmMyWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      // set up layout which will control placement of buttons, etc.
      FlowLayout layout = new FlowLayout(FlowLayout.CENTER, 5, 20);
      frmMyWindow.setLayout(layout);

      // prepare the image label array
      JLabel[] labels = new JLabel[NUM_CARD_IMAGES];
      for (k = 0; k < NUM_CARD_IMAGES; k++)
         labels[k] = new JLabel(icon[k]);

      // place your 3 controls into frame
      for (k = 0; k < NUM_CARD_IMAGES; k++)
         frmMyWindow.add(labels[k]);

      // show everything to the user
      frmMyWindow.setVisible(true);
   }
}
