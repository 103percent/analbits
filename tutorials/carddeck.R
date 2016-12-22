createDeck <- function(totalNumOfDecks = 1)
{
  suits <- c("Diamonds", "Clubs", "Hearts", "Spades")
  cards <- c("Ace", "Deuce", "Three", "Four","Five", 
             "Six", "Seven", "Eight", "Nine", "Ten", 
             "Jack", "Queen", "King")
  values <- c(0,2,3,4,5,
              6,7,8,9,10,
              10,10,10)
  
  deck <- data.frame(Suit=character(0), Card=character(0), Value=numeric(0))
  
  numOfDecks = 1
  
  while (numOfDecks <= totalNumOfDecks){
    for (i in suits){
      for (j in cards){
        deck <- rbind.data.frame(deck, cbind.data.frame(j, i, values[match(j, cards)]))
      }
    }
    numOfDecks = numOfDecks + 1
  }
  
  print(deck)
}