/*
 * Assignment: GUI Cards - Phase 2
 * Names:      Brian Sheridan, Craig Calvert, Kevin Bentley, Samuel Pearce
 * Course:     CST338 - Spring B
 * Date:       04/??/2019
 * Objective:  x
 */

import java.util.Arrays;

public class Assign5phase2
{

   public static void main(String[] args)
   {
      //// ************** Card Testing *********************
      //
      // Create cards for testing
//      System.out.println("-------- Class Card Test --------");
//      Card test = new Card();
//      Card test2 = new Card('N', Card.Suit.diamonds);
//      System.out.println(test.getValue());
//      Card test3 = new Card('J', Card.Suit.clubs);
      //Card test2 = new Card('A', Card.Suit.diamonds);
      //Card test3 = new Card('N', Card.Suit.hearts);
      // Output cards to console
//      System.out.println(test);
//      System.out.println(test2);
//      System.out.println(test3 + "\n");

      // Test set function in card class
//      test.set('N', Card.Suit.diamonds);
//      test2.set('Q', Card.Suit.spades);
//      System.out.println(test);
//      System.out.println(test2);
//      System.out.println(test3);
//      //Tests the equals method
//      System.out.println("\nTest of the equals method");
//      Card test4 = new Card();
//      System.out.println(Card.equals(test4));


      // ************** Hand Testing *********************
      // Create 5 explicit card sets
      //
      // Create cards
      System.out.println("-------- Class Hand Test --------");
      Card card0 = new Card();
      Card card1 = new Card('9', Card.Suit.diamonds);
      Card card2 = new Card('J', Card.Suit.clubs);
      Card card3 = new Card('A', Card.Suit.diamonds);
      Card card4 = new Card('8', Card.Suit.hearts);

      // Create one hand object
      Hand playersHand = new Hand();

      // Loop to populate playersHand with Card objects
      int count = 0;
      int testCardsCount = 0;
      Card[] testCards = new Card[] {card0, card1, card2, card3, card4};

      Card.arraySort(testCards, testCards.length);
      System.out.println("test");

//      while(count < playersHand.MAX_CARDS)
//      {
//         if (testCardsCount < 4)
//         {
//            playersHand.takeCard(testCards[testCardsCount]);
//         }
//         else
//         {
//            testCardsCount = 0;
//            playersHand.takeCard(testCards[testCardsCount]);
//         }
//         count++;
//         testCardsCount++;
//      }
//
//      System.out.println("Hand full\nAfter deal");
//      System.out.println(playersHand.toString());
//      System.out.println("\nTesting inspectCard()");
//      System.out.println(playersHand.inspectCard(4));
//      System.out.println(playersHand.inspectCard(54));
//
//      while (playersHand.getNumCards() > 0)
//      {
//         System.out.println("Playing " + playersHand.playCard());
//      }
//
//      System.out.println("\nAfter playing all cards.");
//      System.out.println(playersHand.toString());

      // ************** Deck Testing *********************
      //    Two decks
      //
      // Test deck class un-shuffled 2 decks
/*      System.out.println("-------- Class Deck Test --------");
//      Deck deck1 = new Deck(2);
//      for(int next = 0; next < (52 * 2) - 1; next++)
//      {
//         System.out.print(deck1.dealCard() + " / ");
//      }
//      // re-initialize deck / shuffle
//      deck1.init(2);
//      deck1.shuffle();
//      System.out.println();
//      // output shuffled deck
//      for(int next = 0; next < (52 * 2) - 1; next++)
//      {
//         System.out.print(deck1.dealCard() + " / ");
//      }
//      System.out.println();
//      //    One Deck
//      // Test deck class un-shuffled 1 decks
//      Deck deck2 = new Deck(1);
//      for(int next = 0; next < (52) - 1 ; next++)
//      {
//         System.out.print(deck2.dealCard() + " / ");
//      }
//      // re-initialize deck / shuffle
//      deck2.init(2);
//      deck2.shuffle();
//      System.out.println();
//      // output shuffled deck
//      for(int next = 0; next < (52) - 1; next++)
//      {
//         System.out.print(deck2.dealCard() + " / ");
//      }
//*/
//      //************** Deck/Hand Testing ****************
//      // Prompt user to input number of hands to deal.
//      Scanner keyboard = new Scanner(System.in);
//      System.out.print("How many hands? (1 - 10, please): ");
//      int numberOfHands = keyboard.nextInt();
//
//      // Check if input is valid. If not prompt user to enter again.
//      while (numberOfHands < 1 || numberOfHands > 10)
//      {
//         System.out.print("The number of hands needs to be between 1 "
//               + "and 10. " + "Please enter again. ");
//         numberOfHands = keyboard.nextInt();
//      }
//      System.out.println("UNSHUFFLED");
//      // Create deck
//      Deck singleDeck1 = new Deck(1);
//      // Create Player hands in a Array
//      Hand player[] = new Hand[numberOfHands];
//      for(int next = 0; next < numberOfHands; next++)
//      {
//         player[next] = new Hand();
//      }
//      // tempory card used for move card from deck to hand
//      Card holder = new Card();
//      // Fill players hands with cards from deck un-shuffled
//      while(holder.getErrorFlag() != true)
//      {
//         for(int next = 0; next < numberOfHands; next++)
//         {
//            holder = singleDeck1.dealCard();
//            if(holder.getErrorFlag() == true)
//            {
//               break;
//            }
//            else
//            {
//               player[next].takeCard(holder);
//            }
//         }
//      }
//      // output to screen players hands
//      for(int next = 0; next < numberOfHands; next++)
//      {
//         System.out.println(player[next].toString());
//         System.out.println();
//      }
//      // Reset all players hands
//      for(int next = 0; next < numberOfHands; next++)
//      {
//         player[next].resetHand();
//      }
//      System.out.println("SHUFFLED");
//      // re-initialize deck and shuffle
//      singleDeck1.init(1);
//      singleDeck1.shuffle();
//      Card holder2 = new Card();
//      // fill players hands with cards from deck
//      while(holder2.getErrorFlag() != true)
//      {
//         for(int next = 0; next < numberOfHands; next++)
//         {
//            holder2 = singleDeck1.dealCard();
//            if(holder2.getErrorFlag() == true)
//            {
//               break;
//            }
//            else
//            {
//               player[next].takeCard(holder2);
//            }
//         }
//      }
//      // output players hands
//      for(int next = 0; next < numberOfHands; next++)
//      {
//         System.out.println(player[next].toString());
//         System.out.println();
//      }
//      // close keyboard
//      keyboard.close();
//      // ************ End Deck/Hand Testing **************
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
      if(newCard.value == card.value && newCard.suit == card.suit)
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
            || value == 'J' || value == 'Q' || value == 'K')
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
      Card newCard = copyCard(card);
      for(int i = 0; i < myCards.length; i++)
         if(myCards[i] == null)
         {
            myCards[i] = newCard;
            numCards++;
            break;
         }

      return true;
   }

   // removes the card in the top occupied position of myCards array and
   // returns it.
   public Card playCard()
   {
      Card cardPlayed = myCards[numCards - 1];
      myCards[numCards - 1] = null;
      numCards--;
      return cardPlayed;
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
    *  with an errorFlage = true is returned.
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

   public void sort(Card[] cards, int arraySize)
   {
      Card.arraySort(cards, arraySize);
   }
}

// ******************** Class Deck ********************
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
      // fills cards with card values from masterPack
      init(numPacks);
   }

   /* Define init
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
         this.numPacks = 1;
      }
      else if((numPacks * 52) > MAX_CARDS)
      {
         totalCards = MAX_CARDS;
         this.numPacks = 6;
      }
      else
      {
         totalCards = numPacks * 52;
         this.numPacks = numPacks;
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
    *   Objective: Return the top card from the deck of cards and remove
    *     it from the deck (set the instance of the card to null.
    *     Increment the topCard variable.
    */
   public Card dealCard()
   {
      // check to see if the top card is valid
      if(this.topCard == (52 * numPacks))
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
