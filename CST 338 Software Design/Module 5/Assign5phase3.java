
/*
 * Assignment: GUI Cards - Phase 3
 * Names:      Brian Sheridan, Craig Calvert, Kevin Bentley, Samuel Pearce
 * Course:     CST338 - Spring B
 * Date:       04/??/2019
 * Objective:  x
 */

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import javax.swing.*;

public class Assign5phase3 implements ActionListener {
   static int NUM_CARDS_PER_HAND = 7;
   static int NUM_PLAYERS = 2;
   static ArrayList<Icon> yourWinnings = new ArrayList<Icon>();
   static ArrayList<Icon> computerWinnings = new ArrayList<Icon>();
   static JLabel[] computerLabels = new JLabel[NUM_CARDS_PER_HAND];
   static JLabel[] humanLabels = new JLabel[NUM_CARDS_PER_HAND];
   static JLabel[] playedCardLabels = new JLabel[NUM_PLAYERS];
   static JLabel[] playLabelText = new JLabel[NUM_PLAYERS];

   public static void main(String[] args)  {

      int numPacksPerDeck = 1;
      int numJokersPerPack = 0;
      int numUnusedCardsPerPack = 0;
      Card[] unusedCardsPerPack = null;
      CardGameFramework highCardGame;
      CardTable myCardTable;
      Random randNum = new Random();
      GUICard.loadCardIcons();
      // establish main frame in which program will run
      myCardTable = new CardTable("CardTable", NUM_CARDS_PER_HAND, NUM_PLAYERS);
      myCardTable.setSize(800, 800);
      myCardTable.setLocationRelativeTo(null);
      myCardTable.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      // show everything to the user
      myCardTable.setVisible(true);
      highCardGame = new CardGameFramework(numPacksPerDeck, numJokersPerPack,
            numUnusedCardsPerPack, unusedCardsPerPack, 
            NUM_PLAYERS, NUM_CARDS_PER_HAND);
      highCardGame.deal();
      Hand yourHand = highCardGame.getHand(0);
      int numYourHand = yourHand.getNumCards();

      /**
       * MyButtonActionListener keeps track of the card ID for the button
       * it's associated with. That way, one listener implementation can
       * handle all of the card buttons.
       */
      final class MyButtonActionListener implements ActionListener
      {
         public int cardNum;
         public MyButtonActionListener(int id)
         {
            this.cardNum = id;
         }
         public void actionPerformed(ActionEvent e) 
         {
            Hand yourHand = highCardGame.getHand(0);
            Hand computerHand = highCardGame.getHand(1);
            int numYourHand = yourHand.getNumCards();
            int numComputerHand = computerHand.getNumCards();

            //Check for an invalid card id
            if(cardNum >= numYourHand)
            {
               return;
            }
            //Remove the played card from the human's hand.
            Card playedCard = yourHand.playCard(cardNum);
            //Update the playing area's card
            myCardTable.clearYourHand();
            numYourHand = yourHand.getNumCards();
            for (int i = 0; i < numYourHand; i++) 
            {
               Icon icon = GUICard.getIcon(yourHand.inspectCard(i));
               // Create a listener for each card in the hand
               MyButtonActionListener listener = new MyButtonActionListener(i);
               myCardTable.addCardToYourHand(icon,listener);
            }
            Icon yourCardIcon = GUICard.getIcon(playedCard);
            myCardTable.setYourCard(yourCardIcon);
            double playerAmount = myCardTable.getCardAmount(playedCard);

            int randCard = randNum.nextInt(numComputerHand);
            Card computerPlayedCard = computerHand.playCard(randCard);
            //Subtract the card we just played.
            numComputerHand -= 1;
            double computerAmount = 
                  myCardTable.getCardAmount(computerPlayedCard);
            Icon computerPlayedIcon = GUICard.getIcon(computerPlayedCard);
            myCardTable.setComputerCard(computerPlayedIcon);

            //Reset the computer hand to the right number of cards
            myCardTable.clearComputerHand();
            for (int i = 0; i < numComputerHand; i++) 
            {
               myCardTable.addCardToComputerHand(GUICard.getBackCardIcon());
            }
            //Evaluate the move
            if (playerAmount > computerAmount)
            {
               myCardTable.setResult("You Win");
               yourWinnings.add(yourCardIcon);
               yourWinnings.add(computerPlayedIcon);
            }
            else
            {
               myCardTable.setResult("Computer Wins");
               computerWinnings.add(yourCardIcon);
               computerWinnings.add(computerPlayedIcon);
            }
         }
      }

      //Load the initial player hand
      for (int i = 0; i < numYourHand; i++) {
         Icon icon = GUICard.getIcon(yourHand.inspectCard(i));
         //Create an action listener for each card with the card id
         //so when it's clicked, we know which one it was
         MyButtonActionListener listener = new MyButtonActionListener(i);
         myCardTable.addCardToYourHand(icon,listener);
      }

      Hand computerHand = highCardGame.getHand(1);
      int numComputerHand = computerHand.getNumCards();

      //Sets the computer hand to only show the back of the cards
      Icon[] back = new Icon[numComputerHand];
      for (int i =0; i < numComputerHand; i++) {
         back[i] = GUICard.getBackCardIcon();
      }
      myCardTable.setComputerHand(back);
      myCardTable.setVisible(true);
   }

   public void actionPerformed(ActionEvent e) {}
}

// ******************** Card Class ********************
class Card {
   private char value;
   private Suit suit;
   private boolean errorFlag;
   public static char[] valuRanks = { 'A', '2', '3', '4', '5', '6', '7', 
         '8', '9', 'T', 'J', 'Q', 'K', 'X' };

   public enum Suit {
      clubs, diamonds, hearts, spades;

      public static Object temp;
   }

   // Card constructor with 2 Parameters
   public Card(char value, Suit suit) {
      // constructor with all param
      set(value, suit);
      this.errorFlag = !isValid(value, suit);

   }

   // Default Card constructor
   public Card() {
      // constructor with no param
      value = 'A';
      suit = Card.Suit.spades;
   }

   // Objective: Return contents of card if the errorFlag equals false
   // if error flag is true return illegal string.
   public String toString() {
      if (errorFlag == true) {
         return ("** illegal **");
      } else {
         return (value + " of " + suit);
      }
   }

   // Objective: sets the value of card if the input parameters are valid
   public boolean set(char value, Suit suit) {
      // Uses the private method isValid
      if (isValid(value, suit) == true) {
         this.value = value;
         this.suit = suit;
         errorFlag = false;
         return true;
      } else {
         errorFlag = true;
         return false;
      }
   }

   // Accessor for card suit
   public Suit getSuit() {
      return this.suit;
   }

   // accessor for card value
   public char getValue() {
      return this.value;
   }

   // accessor for card error flag
   public boolean getErrorFlag() {
      return this.errorFlag;
   }

   // objective: Return a boolean if two cards are equal
   public static boolean equals(Card card)
   {
      Card newCard = new Card();
      if(newCard.value == card.value && newCard.suit == card.suit 
            && newCard.errorFlag == card.errorFlag)
      {
         return true;
      }
      else
      {
         return false;
      }
   }

   // objective: checks for a valid card and returns true/false
   private boolean isValid(char value, Suit suit) {
      if (value == 'A' || value == '2' || value == '3' || value == '4' || 
            value == '5' || value == '6' || value == '7' || value == '8' ||
            value == '9' || value == 'T' || value == 'J' || value == 'Q' ||
            value == 'K' || value == 'X') {
         return true;
      } else {
         return false;
      }
   }

   // Sorts the incoming array of cards using a bubble sort routine.
   static void arraySort(Card[] cards, int arraySize) {
      char cardOne;
      char cardTwo;
      int cardOneValue;
      int cardTwoValue;
      boolean isSorted = false;

      while (!isSorted) {
         isSorted = true;
         for (int i = 0; i < arraySize - 1; i++) {
            cardOne = cards[i].getValue();
            cardTwo = cards[i + 1].getValue();
            // Get the value rank of each card.
            cardOneValue = getCardRank(cardOne);
            cardTwoValue = getCardRank(cardTwo);

            // Compare cards, swap if the first card is higher than the second.
            if (cardOneValue > cardTwoValue) {
               swap(cards, i, i + 1);
               isSorted = false;
            }
         }
         arraySize--;
      }
   }

   // Swaps the two cards being compared in arraySort().
   public static void swap(Card[] cards, int i, int j) {
      Card tempCard = cards[i];
      cards[i] = cards[j];
      cards[j] = tempCard;
   }

   // Checks the value rank of the card and returns the numerical position of
   // the card.
   public static int getCardRank(char cardValue) {
      int i;

      for (i = 0; i < valuRanks.length; i++) {
         if (cardValue == valuRanks[i])
            break;
      }
      return i;
   }

   // Generates a random card.
   public static Card generateRandomCard() {
      Random rand = new Random();

      // Generates a random number to get a card value (A, 2, 3 ... ) from
      // valuRanks.
      int randomNumber1 = rand.nextInt(14);
      char cardValue = valuRanks[randomNumber1];

      // Generates a random number to get a suit (clubs, diamonds, etc.) for
      // the card.
      int randomNumber2 = rand.nextInt(4);
      Suit cardSuit = Suit.values()[randomNumber2];

      // Values for the cardValue and cardSuit are sent to the Card constructor.
      Card randomCard = new Card(cardValue, cardSuit);
      return randomCard;
   }
}

// ******************** Class Hand ********************
class Hand {
   public int MAX_CARDS = 50;
   private int numCards;

   private Card[] myCards;

   // Default hand constructor
   public Hand() {
      myCards = new Card[MAX_CARDS];
   }

   // Resets the players hand
   public void resetHand() {
      Arrays.fill(myCards, null);
      numCards = 0;
   }

   // object copy constructor for takeCard().
   private Card copyCard(Card cardOriginal) {
      // create new instance of Card
      Card cardCopy = new Card(cardOriginal.getValue(), cardOriginal.getSuit());
      return cardCopy;
   }

   // adds a card to the next available position in the myCards array.
   public boolean takeCard(Card card)
   {
      boolean flag = false;
      Card newCard = new Card();
      newCard = this.copyCard(card);
      for(int i = 0; i < myCards.length; i++)
         if(myCards[i] == null)
         {
            myCards[i] = newCard;
            numCards++;
            flag = true;
            break;
         }

      return flag;
   }

   // removes the card in the top occupied position of myCards array and
   // returns it.
   public Card playCard(int cardIndex) {
      if (numCards == 0) // error
      {
         // Creates a card that does not work
         return new Card('M', Card.Suit.spades);
      }
      // Decreases numCards.
      Card card = myCards[cardIndex];

      numCards--;
      for (int i = cardIndex; i < numCards; i++) {
         myCards[i] = myCards[i + 1];
      }

      myCards[numCards] = null;

      return card;
   }

   // Wraps toString() output into multiple lines.
   private String textWrap(String text) {
      String wrappedText = "";
      int widthCount = 1;

      // Loops through string by character, inserting "\n" every 80 characters.
      for (int i = 0; i < text.length(); i++) {
         wrappedText += text.charAt(i);
         widthCount++;
         // When width = 79, "\n" is inserted and width count is reset to one.
         if (widthCount == 79) {
            wrappedText += "\n";
            widthCount = 1;
         }
      }

      return wrappedText;
   }

   // Generates a string of the cards currently in the players hand.
   public String toString() {
      String cards = "";

      for (int i = 0; i < numCards; i++) {
         cards += myCards[i] + ", ";
      }

      // Removes the trailing ", " from the string.
      cards = cards.replaceAll(", $", "");
      String hand = String.format("Hand = ( %s )", cards);
      hand = textWrap(hand);
      return hand;
   }

   // Accessor for numCards
   public int getNumCards() {
      return numCards;
   }

   /*
    * Accessor for an individual card. If card position requested is greater 
    * than the number of cards a hand currently holds a card with an errorFlage
    * = true is returned.
    */
   public Card inspectCard(int k) {
      Card card = new Card();
      if (k > getNumCards()) {
         Card invalid = new Card('N', Card.Suit.diamonds);
         return invalid;
      } else {
         card = myCards[k];
      }

      return card;
   }

   public void sort() {
      sort(myCards, myCards.length);
   }

   public void sort(Card[] cards, int arraySize) {
      Card.arraySort(cards, arraySize);
   }
}

// ******************** Class Deck ********************
class Deck {
   public final int MAX_CARDS = (6 * 56);
   private static Card[] masterPack = new Card[56];
   private Card[] cards;
   private int topCard;
   private int numPacks;

   /*
    * Define Constructor Deck(No input values for deck number) Objective:
    * Initialize the the values in the card class.
    */
   public Deck() {
      allocateMasterPack();
      numPacks = 1;
      init(1);
   }

   /*
    * Define Constructor Deck(input values for deck number) Objective: 
    * Initialize the the values in the card class. Test for input values in
    * range of MAX_CARDS.
    */
   public Deck(int numPacks) {
      allocateMasterPack();
      // fills cards with card values from masterPack
      init(numPacks);
   }

   /*
    * Define init Objective: Checks the range of the inputted number of packs
    * and fills the array of cards with cards from the masterPack.
    */
   public void init(int numPacks) {
      // Verify total number of cards
      int totalCards;
      if (numPacks < 1) {
         totalCards = 56;
         this.numPacks = 1;
      } else if ((numPacks * 56) > MAX_CARDS) {
         totalCards = MAX_CARDS;
         this.numPacks = 6;
      } else {
         totalCards = numPacks * 56;
         this.numPacks = numPacks;
      }
      // set the size of the cards array
      cards = new Card[totalCards];
      // reset topCard
      topCard = 0;
      // Copy cards from masterPack to cards
      for (int next = 0; next < totalCards; next++) {
         this.cards[next] = masterPack[next - (56 * (next / 56))];
      }
   }

   /*
    * Define shuffle Objective: Create two random variables and use them as 
    * indexes to shuffle the deck of cards.
    */
   public void shuffle() {
      Card holder;
      // Loop trough the total of cards times 10
      for (int next = 0; next < (56 * numPacks) * 10; next++) {
         // create random numbers
         int randNumber1 = (int) (Math.random() * (56 * numPacks));
         int randNumber2 = (int) (Math.random() * (56 * numPacks));
         // verify random numbers are not equal to each other
         if (randNumber1 != randNumber2) {
            // Swap the cards in the deck
            holder = cards[randNumber1];
            cards[randNumber1] = cards[randNumber2];
            cards[randNumber2] = holder;
         }
      }
   }

   /*
    * Define dealCard Objective: Return the top card from the deck of cards
    * and remove it from the deck (set the instance of the card to null. 
    * Increment the topCard variable.
    */
   public Card dealCard() {
      // check to see if the top card is valid
      if (this.topCard == (56 * numPacks)) {
         // return invalid card if not valid
         Card invalid = new Card('N', Card.Suit.diamonds);
         return invalid;
      }
      // return the top card from the deck and increment topCard
      Card topCard = cards[this.topCard];
      cards[this.topCard] = null;
      this.topCard++;
      return topCard;
   }

   /*
    * Define Accessor for topCard Objective: Return the top card value
    */
   public int topCard() {
      return topCard;
   }

   /*
    * Define inspectCard Objective: Check to see if current card is valid and
    * return the card If invalid return card with errorFlag set to true 
    * (error flag resides in the Card class)
    */
   public Card inspectCard(int k) {
      // verify parameter 'k' is a valid card and return card
      if (k < (56 * numPacks) - 1 && k >= 0 && cards[k] != null) {
         return cards[k];
      } else {
         // return an invalid card that sets and error flag
         Card invalid = new Card('N', Card.Suit.diamonds);
         return invalid;
      }
   }

   /*
    * Define allocateMasterPack Objective: Fill the materPack with a 
    * standard deck of 52 cards once this method runs it will not run again.
    */
   private static void allocateMasterPack() {
      // check to see if the masterPack is filled if so return
      if (masterPack[0] != null) {
         return;
      }
      // build character set for input
      char value[] = { 'X', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4',
            '3', '2', 'A' };
      // Create a suite address based on required inputs
      Card.Suit suitValue;
      for (int next = 0; next < 56; next++) {
         switch (next / 14) {
         case 0:
            suitValue = Card.Suit.spades;
            break;
         case 1:
            suitValue = Card.Suit.hearts;
            break;
         case 2:
            suitValue = Card.Suit.diamonds;
            break;
         default:
            suitValue = Card.Suit.clubs;
         }
         // Input into the correct position in masterPack
         masterPack[next] = new Card(value[next - (14 * (next / 14))], 
               suitValue);
      }
   }

   // Adds a card to the top of the deck. Prior to adding the card checks that
   // there aren't too many instances of the card already existing.
   public boolean addCard(Card card) {
      // Get the position value of the top card.
      int topCard = topCard();

      // Loop through the deck of cards.
      for (int i = topCard; i < cards.length; i++) {
         if (cards[i].getSuit() == card.getSuit() && cards[i].getValue() == 
               card.getValue()) {
            // False is returned if there are too many instances of the card.
            return false;
         }
      }

      // Card is placed on top of the deck, true is returned.
      cards[topCard - 1] = card;
      return true;
   }

   // Removes a specific card from the deck and places the current top card 
   // into its place.
   public boolean removeCard(Card card) {
      // Get the position value of the top card.
      int topCard = topCard();

      // Loop through the deck of cards.
      for (int i = topCard; i < cards.length; i++) {
         if (cards[i].getSuit() == card.getSuit() && cards[i].getValue() == 
               card.getValue()) {
            // Copy the top card into the removed cards position. Set top card
            // position to null.
            cards[i] = cards[topCard];
            cards[topCard] = null;
            return true;
         }
      }

      // If the card is not in the deck return false.
      return false;
   }

   // Puts all of the cards in the deck back into the right order according to
   // their values.
   public void sort(Card[] cards, int arraySize) {
      Card.arraySort(cards, arraySize);
   }

   // Returns the number of cards remaining in the deck.
   public int getNumCards() {
      int cardCount = 0;

      // Loop through the pack of cards.
      for (int i = 0; i < cards.length; i++) {
         // Add 1 to the card count if card is found.
         if (cards[i] != null) {
            cardCount++;
         }
      }
      // Return the total number of cards in the deck.
      return cardCount;
   }
}

// ----------------------------------------------------------------------

// ----------------------------------------------------------------------

class CardTable extends JFrame implements ActionListener {
   private static final long serialVersionUID = 1L;
   static int MAX_CARDS_PER_HAND = 56;
   static int MAX_PLAYERS = 2; // for now, we only allow 2 person games

   private int numCardsPerHand;
   private int numPlayers;

   // The constructor filters input, adds any panels to the JFrame,
   // and establishes layouts according to the general description below.
   public JPanel pnlComputerHand;
   public JPanel pnlHumanHand;
   public JPanel pnlPlayArea;
   public JLabel win = new JLabel("You Win");
   public JLabel lose = new JLabel("You Lose");
   private JLabel computerCardIcon;
   private JLabel yourCardIcon;
   private JLabel results;

   CardTable(String title, int numCardsPerHand, int numPlayers) {
      super(title);

      LayoutManager layoutManager = new GridLayout(3, 1);
      LayoutManager handLayoutManager = new GridLayout(1, 1);
      LayoutManager cardLayoutManager = new GridLayout(2, 3);

      setLayout(layoutManager);
      pnlComputerHand = new JPanel(handLayoutManager);
      pnlHumanHand = new JPanel(handLayoutManager);
      pnlPlayArea = new JPanel(cardLayoutManager);

      this.numCardsPerHand = Math.min(numCardsPerHand, MAX_CARDS_PER_HAND);
      this.numPlayers = Math.min(numPlayers, MAX_PLAYERS);
      // set up layout which will control placement of buttons, etc.

      // Set panels
      pnlComputerHand.setBorder(BorderFactory.createTitledBorder
            ("Computer Hand"));
      pnlPlayArea.setBorder(BorderFactory.createTitledBorder("Playing Area"));
      pnlHumanHand.setBorder(BorderFactory.createTitledBorder("Your Hand"));
      pnlComputerHand.setVisible(true);
      pnlPlayArea.setVisible(true);
      pnlHumanHand.setVisible(true);

      results = new JLabel("", JLabel.CENTER);
      computerCardIcon = new JLabel("", JLabel.CENTER);
      yourCardIcon = new JLabel("", JLabel.CENTER);

      JLabel placeHolder = new JLabel("", JLabel.CENTER);
      JLabel yourCardLabel = new JLabel("You", JLabel.CENTER);
      JLabel computerCardLabel = new JLabel("Computer", JLabel.CENTER);


      pnlPlayArea.add(computerCardIcon);
      pnlPlayArea.add(results);
      pnlPlayArea.add(yourCardIcon);




      pnlPlayArea.add(computerCardLabel);
      pnlPlayArea.add(placeHolder);
      pnlPlayArea.add(yourCardLabel);


      add(pnlComputerHand);
      add(pnlPlayArea);
      add(pnlHumanHand);

   }

   public void setComputerHand(Icon[] icons) {
      pnlComputerHand.removeAll();

      for (int i = 0; i < icons.length; i++) {
         pnlComputerHand.add(new JLabel(icons[i]));
      }
      pnlComputerHand.revalidate();
      pnlComputerHand.repaint();
      revalidate();
      repaint();
   }


   public void clearYourHand()
   {
      pnlHumanHand.removeAll();
      pnlHumanHand.revalidate();
      pnlHumanHand.repaint();
   }
   public void addCardToYourHand(Icon icon, ActionListener listener)
   {
      JButton btn = new JButton(icon);
      btn.addActionListener(listener);
      pnlHumanHand.add(btn);
      pnlHumanHand.revalidate();
      pnlHumanHand.repaint();
   }

   public void clearComputerHand()
   {
      pnlComputerHand.removeAll();
      pnlComputerHand.revalidate();
      pnlComputerHand.repaint();
   }
   public void addCardToComputerHand(Icon icon)
   {
      JButton btn = new JButton(icon);
      pnlComputerHand.add(btn);
      pnlComputerHand.revalidate();
      pnlComputerHand.repaint();
   }

   public void setComputerCard(Icon icon) {
      computerCardIcon.setIcon(icon);
      pnlPlayArea.repaint();
   }

   //this area to send your selected card to the playArea
   public void setYourCard(Icon icon) {
      yourCardIcon.setIcon(icon);
      pnlPlayArea.repaint();
   }

   public void setResult(String status) {
      results.setText(status);
      Font bigger = new Font("TimesRoman",Font.BOLD,25);
      results.setFont(bigger);
      pnlPlayArea.repaint();
   }

   // Accessor for number of cards per hand
   public int numCardsPerHand() {
      return numCardsPerHand;
   }

   // Accessor for number of players
   public int numPlayers() {
      return numPlayers;
   }

   public double getCardAmount(Card card)
   {
       double rank = (double)Card.getCardRank(card.getValue());

       switch (card.getSuit()) {
        case clubs:
           return rank + 0.1;
        case diamonds:
            return rank + 0.2;
        case hearts:
            return rank + 0.3;
        case spades:
            return rank + 0.4;
        default:
           return 0;
        }
   }

   // show everything to the user
   public void actionPerformed(ActionEvent e) 
   {

   }


}

class GUICard {
   static int NUM_CARD_VALUES = 14;
   static int NUM_CARD_SUITS = 4;
   static Icon[][] icon = new 
         ImageIcon[NUM_CARD_VALUES][NUM_CARD_SUITS]; // 14 = A thru K + joker
   private static Icon iconBack;
   static boolean iconsLoaded = false;
   public static char[] valueRanks = { '2', '3', '4', '5', '6', '7', '8',
         '9', 'J', 'Q', 'K', 'A', 'X' };

   static void loadCardIcons() {
      String suit;
      String cardValue;

      // Builds the file names ("AC.gif", "2C.gif", "3C.gif", "TC.gif", etc.)
      // and inserts them into the ImageIcon array.
      for (int suitCount = 0; suitCount < 4; suitCount++) {
         suit = turnIntIntoCardSuit(suitCount);
         for (int valueCount = 0; valueCount < 14; valueCount++) {
            cardValue = turnIntIntoCardValue(valueCount);
            icon[valueCount][suitCount] = new ImageIcon(GUICard.class.
                  getResource("images/" + cardValue + suit + ".gif"));
         }
      }

      // Adds the card-back image icon
      iconBack = new ImageIcon(GUICard.class.getResource("images/BK.gif"));
   }

   static public int valueAsInt(Card card) {
      return Card.getCardRank(card.getValue());
   }

   static public Icon getIcon(Card card) {
      return icon[valueAsInt(card)][suitAsInt(card)];
   }

   static public int suitAsInt(Card card) {
      switch (card.getSuit()) {
      case clubs:
         return 0;
      case diamonds:
         return 1;
      case hearts:
         return 2;
      case spades:
         return 3;
      default:
         return 0;
      }
   }
   static public Icon joker() {
      return new ImageIcon(GUICard.class.getResource("images/XS.gif"));
   }
   static public Icon getBackCardIcon() {
      return iconBack;
   }

   // turns 0 - 13 into "A", "2", "3", ... "Q", "K", "X"
   static String turnIntIntoCardValue(int k) {
      String[] cardValue = { "A", "2", "3", "4", "5", "6", "7", "8", "9", 
            "T", "J", "Q", "K", "X" };
      return cardValue[k];
   }

   // turns 0 - 3 into "C", "D", "H", "S"
   static String turnIntIntoCardSuit(int j) {
      String[] suit = { "C", "D", "H", "S" };
      return suit[j];
   }

}

//class CardGameFramework  ----------------------------------------------------
class CardGameFramework {
   private static final int MAX_PLAYERS = 50;

   private int numPlayers;
   private int numPacks; // # standard 52-card packs per deck
   // ignoring jokers or unused cards
   private int numJokersPerPack; // if 2 per pack & 3 packs per deck, get 6
   private int numUnusedCardsPerPack; // # cards removed from each pack
   private int numCardsPerHand; // # cards to deal each player
   private Deck deck; // holds the initial full deck and gets
   // smaller (usually) during play
   private Hand[] hand; // one Hand for each player
   private Card[] unusedCardsPerPack; // an array holding the cards not used
   // in the game. e.g. pinochle does not
   // use cards 2-8 of any suit

   public CardGameFramework(int numPacks, int numJokersPerPack, 
         int numUnusedCardsPerPack, Card[] unusedCardsPerPack,  int numPlayers,
         int numCardsPerHand) {
      int k;

      // filter bad values
      if (numPacks < 1 || numPacks > 6)
         numPacks = 1;
      if (numJokersPerPack < 0 || numJokersPerPack > 4)
         numJokersPerPack = 0;
      if (numUnusedCardsPerPack < 0 || numUnusedCardsPerPack > 50) // > 1 card
         numUnusedCardsPerPack = 0;
      if (numPlayers < 1 || numPlayers > MAX_PLAYERS)
         numPlayers = 4;
      // one of many ways to assure at least one full deal to all players
      if (numCardsPerHand < 1 || numCardsPerHand > numPacks * 
            (52 - numUnusedCardsPerPack) / numPlayers) numCardsPerHand = 
            numPacks * (52 - numUnusedCardsPerPack) / numPlayers;

      // allocate
      this.unusedCardsPerPack = new Card[numUnusedCardsPerPack];
      this.hand = new Hand[numPlayers];
      for (k = 0; k < numPlayers; k++)
         this.hand[k] = new Hand();
      deck = new Deck(numPacks);

      // assign to members
      this.numPacks = numPacks;
      this.numJokersPerPack = numJokersPerPack;
      this.numUnusedCardsPerPack = numUnusedCardsPerPack;
      this.numPlayers = numPlayers;
      this.numCardsPerHand = numCardsPerHand;
      for (k = 0; k < numUnusedCardsPerPack; k++)
         this.unusedCardsPerPack[k] = unusedCardsPerPack[k];

      // prepare deck and shuffle
      newGame();
   }

   // constructor overload/default for game like bridge
   public CardGameFramework() {
      this(1, 0, 0, null, 4, 13);
   }

   public Hand getHand(int k) {
      // hands start from 0 like arrays

      // on error return automatic empty hand
      if (k < 0 || k >= numPlayers)
         return new Hand();

      return hand[k];
   }

   public Card getCardFromDeck() {
      return deck.dealCard();
   }

   public int getNumCardsRemainingInDeck() {
      return deck.getNumCards();
   }

   public void newGame() {
      int k, j;

      // clear the hands
      for (k = 0; k < numPlayers; k++)
         hand[k].resetHand();

      // restock the deck
      deck.init(numPacks);

      // remove unused cards
      for (k = 0; k < numUnusedCardsPerPack; k++)
         deck.removeCard(unusedCardsPerPack[k]);

      // add jokers
      for (k = 0; k < numPacks; k++)
         for (j = 0; j < numJokersPerPack; j++)
            deck.addCard(new Card('X', Card.Suit.values()[j]));

      // shuffle the cards
      deck.shuffle();
   }

   public boolean deal() {
      // returns false if not enough cards, but deals what it can
      int k, j;
      boolean enoughCards;

      // clear all hands
      for (j = 0; j < numPlayers; j++)
         hand[j].resetHand();

      enoughCards = true;
      for (k = 0; k < numCardsPerHand && enoughCards; k++) {
         for (j = 0; j < numPlayers; j++)
            if (deck.getNumCards() > 0)
               hand[j].takeCard(deck.dealCard());
            else {
               enoughCards = false;
               break;
            }
      }

      return enoughCards;
   }

   void sortHands() {
      int k;

      for (k = 0; k < numPlayers; k++)
         hand[k].sort();
   }

   Card playCard(int playerIndex, int cardIndex) {
      // returns bad card if either argument is bad
      if (playerIndex < 0 || playerIndex > numPlayers - 1 || cardIndex < 0 
            || cardIndex > numCardsPerHand - 1) {
         // Creates a card that does not work
         return new Card('M', Card.Suit.spades);
      }

      // return the card played
      return hand[playerIndex].playCard(cardIndex);

   }

   boolean takeCard(int playerIndex) {
      // returns false if either argument is bad
      if (playerIndex < 0 || playerIndex > numPlayers - 1)
         return false;

      // Are there enough Cards?
      if (deck.getNumCards() <= 0)
         return false;

      return hand[playerIndex].takeCard(deck.dealCard());
   }
}


