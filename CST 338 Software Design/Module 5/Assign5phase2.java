/*
 * Assignment: GUI Cards - Phase 2
 * Names:      Brian Sheridan, Craig Calvert, Kevin Bentley, Samuel Pearce
 * Course:     CST338 - Spring B
 * Date:       04/09/2019
 * Objective:  Create a program with a separate CardTable class that extends
 *             JFrame. This class will control the positioning of the panels and
 *             cards of the GUI.
 */

import java.awt.*;
import java.util.Arrays;
import java.util.Random;
import javax.swing.*;

public class Assign5phase2
{
   static int NUM_CARDS_PER_HAND = 7;
   static int  NUM_PLAYERS = 2;
//   static JLabel[] computerLabels = new JLabel[NUM_CARDS_PER_HAND];
//   static JLabel[] humanLabels = new JLabel[NUM_CARDS_PER_HAND];
//   static JLabel[] playedCardLabels  = new JLabel[NUM_PLAYERS];
//   static JLabel[] playLabelText  = new JLabel[NUM_PLAYERS];

   public static void main(String[] args)
   {
      GUICard.loadCardIcons();
      // Create main frame in which program will run.
      CardTable myCardTable 
      = new CardTable("CardTable", NUM_CARDS_PER_HAND, NUM_PLAYERS);
      myCardTable.setSize(800, 800);
      myCardTable.setLocationRelativeTo(null);
      myCardTable.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

//      // show everything to the user
//      myCardTable.setVisible(true);

      Deck deck1 = new Deck();
      deck1.shuffle();
      Icon iconsComputer[] = new Icon[NUM_CARDS_PER_HAND];
      Icon iconsPlayer[] = new Icon[NUM_CARDS_PER_HAND];
      Hand computerHand = new Hand();
      Hand playerHand = new Hand();

      // Loop deals the cards to the computer and player hands.
      for(int next = 0; next < NUM_CARDS_PER_HAND; next++)
      {
         computerHand.takeCard(deck1.dealCard());
         playerHand.takeCard(deck1.dealCard());
         iconsComputer[next] = GUICard.getBackCardIcon();
         iconsPlayer[next] = GUICard.getIcon(playerHand.inspectCard(next));
      }
      // Set the icons to be displayed for both the computer and player hands.
      myCardTable.setComputerHand(iconsComputer);
      myCardTable.setYourHand(iconsPlayer);

      // Generate two random cards to be positioned in the play region.
      myCardTable.setYourCard(GUICard.getIcon(Card.generateRandomCard()));
      myCardTable.setComputerCard(GUICard.getIcon(Card.generateRandomCard()));

      // show everything to the user
      myCardTable.setVisible(true);
   }

}

// ******************** Card Class ********************
class Card
{
   private char value;
   private Suit suit;
   private boolean errorFlag;
   public static char[] valuRanks = {'A', '2', '3', '4', '5', '6', '7', '8',
         '9', 'T', 'J', 'Q', 'K', 'X'};
   public enum Suit
   {
      clubs,
      diamonds,
      hearts,
      spades;

      public static Object temp;
   }
   // Card constructor with 2 Parameters
   public Card(char value, Suit suit)
   {
      //constructor with all param
      set(value, suit);
      this.errorFlag = !isValid(value, suit);
   }
   // Default Card constructor
   public Card()
   {
      //constructor with no param
      value = 'A';
      suit = Card.Suit.spades;
   }

   // Objective: Return contents of card if the errorFlag equals false
   //      if error flag is true return illegal string.
   public String toString()
   {
      if(errorFlag == true)
      {
         return ("** illegal **");
      }
      else
      {
         return (value + " of " + suit);
      }
   }

   // Objective: sets the value of card if the input parameters are valid
   public boolean set(char value, Suit suit)
   {
      // Uses the private method isValid
      if(isValid(value, suit) == true)
      {
         this.value = value;
         this.suit = suit;
         errorFlag = false;
         return true;
      }
      else
      {
         errorFlag = true;
         return false;
      }
   }

   // Accessor for card suit
   public Suit getSuit()
   {
      return this.suit;
   }

   // accessor for card value
   public char getValue()
   {
      return this.value;
   }

   // accessor for card error flag
   public boolean getErrorFlag()
   {
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
   private boolean isValid(char value, Suit suit)
   {
      if(value == 'A' || value == '2' || value == '3' || value == '4'
            || value == '5' || value == '6' || value == '7'
            || value == '8' || value == '9' || value == 'T'
            || value == 'J' || value == 'Q' || value == 'K'
            || value == 'X')
      {
         return true;
      }
      else
      {
         return false;
      }
   }

   // Sorts the incoming array of cards using a bubble sort routine.
   static void arraySort(Card[] cards, int arraySize)
   {
      char cardOne;
      char cardTwo;
      int cardOneValue;
      int cardTwoValue;
      boolean isSorted = false;

      while (!isSorted)
      {
         isSorted = true;
         for(int i = 0; i < arraySize - 1; i++)
         {
            cardOne = cards[i].getValue();
            cardTwo = cards[i + 1].getValue();
            // Get the value rank of each card.
            cardOneValue = getCardRank(cardOne);
            cardTwoValue = getCardRank(cardTwo);

            // Compare cards, swap if the first card is higher than the second.
            if(cardOneValue > cardTwoValue)
            {
               swap(cards, i, i + 1);
               isSorted = false;
            }
         }
         arraySize--;
      }
   }

   // Swaps the two cards being compared in arraySort().
   public static void swap(Card[] cards, int i, int j)
   {
      Card tempCard = cards[i];
      cards[i] = cards[j];
      cards[j] = tempCard;
   }

   // Checks the value rank of the card and returns the numerical position of
   // the card.
   public static int getCardRank(char cardValue)
   {
      int i;

      for(i = 0; i < valuRanks.length; i++)
      {
         if (cardValue == valuRanks[i])
            break;
      }
      return i;
   }

   // Generates a random card.
   public static Card generateRandomCard()
   {
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
class Hand
{
   public int MAX_CARDS = 50;
   private int numCards;

   private Card[] myCards;

   // Default hand constructor
   public Hand()
   {
      myCards = new Card[MAX_CARDS];
   }

   // Resets the players hand
   public void resetHand()
   {
      Arrays.fill(myCards, null );
      numCards = 0;
   }

   // object copy constructor for takeCard().
   private Card copyCard(Card cardOriginal)
   {
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
   public Card playCard(int cardIndex)
   {
      if ( numCards == 0 ) //error
      {
         //Creates a card that does not work
         return new Card('M', Card.Suit.spades);
      }
      //Decreases numCards.
      Card card = myCards[cardIndex];

      numCards--;
      for(int i = cardIndex; i < numCards; i++)
      {
         myCards[i] = myCards[i+1];
      }

      myCards[numCards] = null;

      return card;
   }

   // Wraps toString() output into multiple lines.
   private String textWrap(String text)
   {
      String wrappedText = "";
      int widthCount = 1;

      // Loops through string by character, inserting "\n" every 80 characters.
      for (int i = 0; i < text.length(); i++)
      {
         wrappedText += text.charAt(i);
         widthCount++;
         // When width = 79, "\n" is inserted and width count is reset to one.
         if (widthCount == 79)
         {
            wrappedText += "\n";
            widthCount = 1;
         }
      }

      return wrappedText;
   }

   // Generates a string of the cards currently in the players hand.
   public String toString()
   {
      String cards = "";

      for(int i = 0; i < numCards; i++)
      {
         cards += myCards[i] + ", ";
      }

      // Removes the trailing ", " from the string.
      cards = cards.replaceAll(", $", "");
      String hand = String.format("Hand = ( %s )", cards);
      hand = textWrap(hand);
      return hand;
   }

   // Accessor for numCards
   public int getNumCards()
   {
      return numCards;
   }

   /* Accessor for an individual card. If card position requested is
    *  greater than the number of cards a hand currently holds a card
    *  with an errorFlag = true is returned.
    */
   public Card inspectCard(int k)
   {
      Card card = new Card();
      if (k > getNumCards())
      {
         Card invalid = new Card('N', Card.Suit.diamonds);
         return invalid;
      }
      else
      {
         card = myCards[k];
      }

      return card;
   }

   public void sort()
   {
      sort(myCards,myCards.length);
   }

   public void sort(Card[] cards, int arraySize)
   {
      Card.arraySort(cards, arraySize);
   }
}

// ******************** Class Deck ********************
class Deck
{
   public final int MAX_CARDS = (6*56);
   private static Card[] masterPack = new Card[56];
   private Card[] cards;
   private int topCard;
   private int numPacks;

   /* Define Constructor Deck(No input values for deck number)
    *   Objective: Initialize the the values in the card class.
    */
   public Deck()
   {
      allocateMasterPack();
      numPacks = 1;
      init(1);
   }

   /* Define Constructor Deck(input values for deck number)
    *   Objective: Initialize the the values in the card class. Test
    *   for input values in range of MAX_CARDS.
    */
   public Deck(int numPacks)
   {
      allocateMasterPack();
      // fills cards with card values from masterPack
      init(numPacks);
   }

   /* Define init
    *   Objective: Checks the range of the inputted number of packs
    *   and fills the array of cards with cards from the masterPack.
    */
   public void init(int numPacks)
   {
      // Verify total number of cards
      int totalCards;
      if(numPacks < 1)
      {
         totalCards = 56;
         this.numPacks = 1;
      }
      else if((numPacks * 56) > MAX_CARDS)
      {
         totalCards = MAX_CARDS;
         this.numPacks = 6;
      }
      else
      {
         totalCards = numPacks * 56;
         this.numPacks = numPacks;
      }
      // set the size of the cards array
      cards = new Card[totalCards];
      // reset topCard
      topCard = 0;
      // Copy cards from masterPack to cards
      for(int next = 0; next < totalCards; next++)
      {
         this.cards[next] = masterPack[next - (56 * (next/56))];
      }
   }

   /* Define shuffle
    *   Objective: Create two random variables and use them as indexes to
    *     shuffle the deck of cards.
    */
   public void shuffle()
   {
      Card holder;
      // Loop trough the total of cards times 10
      for (int next = 0; next < (56 * numPacks) * 10; next ++)
      {
         // create random numbers
         int randNumber1 = ( int )(Math.random() * (56 * numPacks));
         int randNumber2 = ( int )(Math.random() * (56 * numPacks));
         // verify random numbers are not equal to each other
         if (randNumber1 != randNumber2)
         {
            // Swap the cards in the deck
            holder = cards[randNumber1];
            cards[randNumber1] = cards[randNumber2];
            cards[randNumber2] = holder;
         }
      }
   }

   /* Define dealCard
    *   Objective: Return the top card from the deck of cards and remove
    *     it from the deck (set the instance of the card to null.
    *     Increment the topCard variable.
    */
   public Card dealCard()
   {
      // check to see if the top card is valid
      if(this.topCard == (56 * numPacks))
      {
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

   /* Define Accessor for topCard
    *   Objective: Return the top card value
    */
   public int topCard()
   {
      return topCard;
   }

   /* Define inspectCard
    *   Objective: Check to see if current card is valid and return the card
    *     If invalid return card with errorFlag set to true (error flag
    *     resides in the Card class)
    */
   public Card inspectCard(int k)
   {
      // verify parameter 'k' is a valid card and return card
      if(k < (56 * numPacks) - 1 && k >= 0 && cards[k] != null)
      {
         return cards[k];
      }
      else
      {
         // return an invalid card that sets and error flag
         Card invalid = new Card('N', Card.Suit.diamonds);
         return invalid;
      }
   }

   /* Define allocateMasterPack
    *   Objective: Fill the materPack with a standard deck of 52 cards
    *   once this method runs it will not run again.
    */
   private static void allocateMasterPack()
   {
      //check to see if the masterPack is filled if so return
      if (masterPack[0] != null)
      {
         return;
      }
      // build character set for input
      char value[] = {'X','K','Q','J','T','9','8','7','6','5','4','3','2','A'};
      // Create a suite address based on required inputs
      Card.Suit suitValue;
      for (int next = 0; next < 56; next++)
      {
         switch(next / 14)
         {
         case 0:
            suitValue =  Card.Suit.spades;
            break;
         case 1:
            suitValue = Card.Suit.hearts;
            break;
         case 2:
            suitValue =  Card.Suit.diamonds;
            break;
         default:
            suitValue =  Card.Suit.clubs;
         }
         // Input into the correct position in masterPack
         masterPack[next] = new Card(value[next - (14 * (next/14))],suitValue);
      }
   }

   // Adds a card to the top of the deck. Prior to adding the card checks that
   // there aren't too many instances of the card already existing.
   public boolean addCard(Card card)
   {
      // Get the position value of the top card.
      int topCard = topCard();

      // Loop through the deck of cards.
      for(int i = topCard; i < cards.length; i++)
      {
         if (cards[i].getSuit() == card.getSuit() && cards[i].getValue() ==
               card.getValue())
         {
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
   public boolean removeCard(Card card)
   {
      // Get the position value of the top card.
      int topCard = topCard();

      // Loop through the deck of cards.
      for(int i = topCard; i < cards.length; i++)
      {
         if (cards[i].getSuit() == card.getSuit() && cards[i].getValue() ==
               card.getValue())
         {
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
   public void sort(Card[] cards, int arraySize)
   {
      Card.arraySort(cards, arraySize);
   }

   // Returns the number of cards remaining in the deck.
   public int getNumCards()
   {
      int cardCount = 0;

      // Loop through the pack of cards.
      for (int i = 0; i < cards.length; i++)
      {
         // Add 1 to the card count if card is found.
         if (cards[i] != null)
         {
            cardCount++;
         }
      }
      // Return the total number of cards in the deck.
      return cardCount;
   }
}

// ****************** Class CardTable *****************
class CardTable extends JFrame
{
   private static final long serialVersionUID = 1L;
   static int MAX_CARDS_PER_HAND = 56;
   static int MAX_PLAYERS = 2;  // for now, we only allow 2 person games

   private int numCardsPerHand;
   private int numPlayers;

   // The constructor filters input, adds any panels to the JFrame, 
   // and establishes layouts according to the general description below.
   public JPanel pnlComputerHand;
   public JPanel pnlHumanHand;
   public JPanel pnlPlayArea;
   private JLabel computerCardIcon;
   private JLabel yourCardIcon;

   CardTable(String title, int numCardsPerHand, int numPlayers)
   {
      super(title);

      LayoutManager layoutManager = new GridLayout(3,1);
      LayoutManager handLayoutManager = new GridLayout(1, 0);
      LayoutManager cardLayoutManager = new GridLayout(2,2);

      setLayout(layoutManager);
      pnlComputerHand = new JPanel(handLayoutManager);
      pnlPlayArea = new JPanel(cardLayoutManager);
      pnlHumanHand = new JPanel(handLayoutManager);


      this.numCardsPerHand = Math.min(numCardsPerHand, MAX_CARDS_PER_HAND);
      this.numPlayers = Math.min(numPlayers, MAX_PLAYERS);
      // set up layout which will control placement of buttons, etc.

      // Set panels
      pnlComputerHand.setBorder(BorderFactory
            .createTitledBorder("Computer Hand"));
      pnlPlayArea.setBorder(BorderFactory.createTitledBorder("Playing Area"));
      pnlHumanHand.setBorder(BorderFactory.createTitledBorder("Your Hand"));
      pnlComputerHand.setVisible(true);
      pnlPlayArea.setVisible(true);
      pnlHumanHand.setVisible(true);

      computerCardIcon = 
            new JLabel(GUICard.getBackCardIcon(), JLabel.CENTER );
      yourCardIcon =
            new JLabel(GUICard.getBackCardIcon(), JLabel.CENTER );

      JLabel computerCardLabel = new JLabel( "Computer", JLabel.CENTER );
      JLabel yourCardLabel = new JLabel( "You", JLabel.CENTER );
      pnlPlayArea.add(computerCardIcon);
      pnlPlayArea.add(yourCardIcon);
      pnlPlayArea.add(computerCardLabel);
      pnlPlayArea.add(yourCardLabel);

      add(pnlComputerHand);
      add(pnlPlayArea);
      add(pnlHumanHand);
   }

   public void setComputerHand(Icon[] icons)
   {
      pnlComputerHand.removeAll();

      for(int i=0;i<icons.length;i++)
      {
         pnlComputerHand.add(new JLabel(icons[i]));
      }
      pnlComputerHand.revalidate();
      pnlComputerHand.repaint();
      revalidate();
      repaint();
   }

   public void setYourHand(Icon[] icons)
   {
      pnlHumanHand.removeAll();
      for(int i=0;i<icons.length;i++)
      {
         pnlHumanHand.add(new JLabel(icons[i]));
      }
      pnlHumanHand.revalidate();
      pnlHumanHand.repaint();
   }

   public void setComputerCard(Icon icon)
   {
      computerCardIcon.setIcon(icon);
      pnlPlayArea.revalidate();
      pnlPlayArea.repaint();
   }

   public void setYourCard(Icon icon)
   {
      yourCardIcon.setIcon(icon);
      pnlPlayArea.revalidate();
      pnlPlayArea.repaint();
   }

   // Accessor for number of cards per hand
   public int numCardsPerHand()
   {
      return numCardsPerHand;
   }

   // Accessor for number of players
   public int numPlayers()
   {
      return numPlayers;
   }
}

// ******************* Class GUICard ******************
class GUICard
{
   static int NUM_CARD_VALUES = 14;
   static int NUM_CARD_SUITS = 4;
   static Icon[][] icon = new 
         ImageIcon[NUM_CARD_VALUES][NUM_CARD_SUITS]; // 14 = A thru K + joker
   private static Icon iconBack;
//   static boolean iconsLoaded = false;
//   public static char[] valueRanks =
//      {'2','3','4','5','6','7','8','9','J','Q','K','A','X'};

   // Stores to Card icons into a 2-D array.
   static void loadCardIcons()
   {
      String suit;
      String cardValue;

      // Builds the file names("AC.gif", "2C.gif", "3C.gif", "TC.gif", etc.)
      // and inserts them into the ImageIcon array.
      for (int suitCount = 0; suitCount < 4; suitCount++)
      {
         suit = turnIntIntoCardSuit(suitCount);
         for (int valueCount = 0; valueCount < 14; valueCount++)
         {
            cardValue = turnIntIntoCardValue(valueCount);
            icon[valueCount][suitCount] = new ImageIcon(GUICard.class.
                  getResource("images/" + cardValue + suit + ".gif"));
         }
      }

      // Adds the card-back image icon
      iconBack = new ImageIcon(GUICard.class.getResource("images/BK.gif"));
   }

   // Takes a Card object and returns the int rank value of the card.
   static public int valueAsInt(Card card)
   {
      return Card.getCardRank(card.getValue());
   }

   // Takes a Card object from the client, and returns the Icon for that card.
   static public Icon getIcon(Card card)
   {
      return icon[valueAsInt(card)][suitAsInt(card)];   
   }

   // Takes a Card object and returns the int value of the cards suit.
   static public int suitAsInt(Card card)
   {
      switch(card.getSuit())
      {
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

   // Returns the icon for the back-of-card
   static public Icon getBackCardIcon()
   {
      return iconBack;   
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
}
