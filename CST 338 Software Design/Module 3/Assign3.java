/*
 * Assignment 3 Deck of Cards
 * Brian Sheridan, Craig Calvert, Kevin Bentley, Samuel Pearce
 * Objective: 
 */

public class Assign3 
{

   public static void main(String[] args) 
   {
//      Card test = new Card();
//      Card test2 = new Card('N', Card.Suit.diamonds);
//      Card test3 = new Card('J', Card.Suit.clubs);
//      //Card test2 = new Card('A', Card.Suit.diamonds);
//      //Card test3 = new Card('N', Card.Suit.hearts);
//      System.out.println(test);
//      System.out.println(test2);
//      System.out.println(test3 + "\n");
//      
//      test.set('N', Card.Suit.diamonds);
//      test2.set('Q', Card.Suit.spades);
//      System.out.println(test);
//      System.out.println(test2);
//      System.out.println(test3);
//      /*
//      //Tests the equals method
//      Card test4 = new Card();
//      System.out.println(Card.equals(test4));
//      */
// ************** Deck Testing *********************      
//    Two decks
      Deck test = new Deck(2);
      for(int next = 0; next < (52 * 2) - 1; next++)
      {
         System.out.print(test.dealCard() + " / ");
      }
      test.init(2);
      test.shuffle();
      System.out.println();
      for(int next = 0; next < (52 * 2) - 1; next++)
      {
         System.out.print(test.dealCard() + " / ");
      }
      System.out.println();
//    One Deck  
      Deck test2 = new Deck(1);
      for(int next = 0; next < (52) - 1 ; next++)
      {
         System.out.print(test2.dealCard() + " / ");
      }
      test2.init(2);
      test2.shuffle();
      System.out.println();
      for(int next = 0; next < (52) - 1; next++)
      {
         System.out.print(test2.dealCard() + " / ");
      }
   }
}
class Card
{
   private char value;
   private Suit suit;
   private boolean errorFlag;
   public enum Suit
   {
      clubs,
      diamonds,
      hearts,
      spades;

      public static Object temp;
   }
   public Card(char value, Suit suit)
   {
      //constructor with all param
      set(value, suit);
      getErrorFlag();
      
   }
   public Card()
   {
      //constructor with no param
      value = 'A';
      suit = Card.Suit.spades;
   }
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
   public Suit getSuit()
   {
      return this.suit;
   }
   public char getValue()
   {
      return this.value;
   }
   public boolean getErrorFlag()
   {
      return this.errorFlag;
   }
   public static boolean equals(Card card)
   {
      Card newCard = new Card();
      if(newCard.value == card.value && newCard.suit == newCard.suit)
      {
         return true;
      }
      else
      {
         return false;
      }
   }
   private boolean isValid(char value, Suit suit)
   {
      if(value == 'A' || value == '2' || value == '3' || value == '4'
            || value == '5' || value == '6' || value == '7'
            || value == '8' || value == '9' || value == 'T' 
            || value == 'J' || value == 'Q' || value == 'K')
      {
         return true;
      }
      else
      {
         return false;
      }   
   }   
}

/* Define Class Deck
 *   Constant Variables:
 *     MAX_CARDS    -> Max number of Cards allowed (Type INT)
 *   Static Variables:
 *     masterPack   -> Master Deck (Type Array of cards)
 *     Card[]       -> Current Working Deck (Type Array of cards)
 *     string3      -> Wheel 3 (Type String)
 *     topCard      -> Tracks the top card on the deck (Type INT)
 *     numPacks     -> Total decks used in cards (Type INT)
 *   Objective: Use the card class to build a deck of card from a given
 *     number of decks. this class is used to deal cards to the hand class. 
 */  
class Deck 
{
   public final int MAX_CARDS = (6*52);
   private static Card[] masterPack = new Card[52];
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
      // Verifies packs entered are less then 1
      if(numPacks < 1) 
      {
         this.numPacks = 1;
       
      }
      // Verifies packs entered are below MAX_CARDS 
      else if((numPacks * 52) > MAX_CARDS) 
      {
         this.numPacks = 6;
      }
      else 
      {
         this.numPacks = numPacks; // set class variable
      }
      // fills cards with card values from masterPack
      init(this.numPacks);  
   }

   /* Define init
    *   Static Variables:
    *     totalCards       -> Get total count of cards (Type INT)    
    *   Objective: Checks the range of the inputed number of packs 
    *   and fills the array of cards with cards from the masterPack.
    */    
   public void init(int numPacks)
   {
      // Verify total number of cards
      int totalCards;
      if(numPacks < 1) 
      {
         totalCards = 52;
       
      }
      else if((numPacks * 52) > MAX_CARDS) 
      {
         totalCards = MAX_CARDS;
      }
      else 
      {
         totalCards = numPacks * 52;
      }
      // set the size of the cards array  
      cards = new Card[totalCards];
      // reset topCard
      topCard = 0;
      // Copy cards from masterPack to cards
      for(int next = 0; next < totalCards; next++) 
      {
         this.cards[next] = masterPack[next - (52 * (next/52))]; 
      }
      
   }
   
   /* Define shuffle
    *   Object Variables:
    *     holder       -> Temp storage for moving cards (Type Card) 
    *   Static Variables:
    *     randNumber1  -> Random number for index 1 (Type INT)
    *     randNumber2  -> Random number for index 2 (Type INT)      
    *   Objective: Create two random variables and use them as indexes to 
    *     shuffle the deck of cards.
    */ 
   public void shuffle()
   {
      Card holder;
      // Loop trough the total of cards times 10
      for (int next = 0; next < (52 * numPacks) * 10; next ++) 
      {
         // create random numbers
         int randNumber1 = ( int )(Math.random() * (52 * numPacks));
         int randNumber2 = ( int )(Math.random() * (52 * numPacks));
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
    *   Object Variables:
    *     invalid       -> used if cards are all used (Type Card) 
    *
    *   Objective: Return the top card from the deck of cards and remove 
    *     it from the deck (set the instance of the card to null.
    *     Increment the topCard variable.
    */ 
   public Card dealCard()
   {
      // check to see if the top card is valid 
      if(this.topCard == (52 * numPacks) - 1)
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
      if(k < (52 * numPacks) - 1 && k >= 0 && cards[k] != null) 
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
    *   Static Variables:
    *     value          -> Setup a char list for input (Type CHAR)
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
      char value[] = {'K','Q','J','T','9','8','7','6','5','4','3','2','A'};
      // Create a suite address based on required inputs
      Card.Suit suitValue;
      for (int next = 0; next < 52; next++) 
      {
         switch(next / 13) 
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
         masterPack[next] = new Card(value[next - (13 * (next/13))],suitValue);
      }
   }
}