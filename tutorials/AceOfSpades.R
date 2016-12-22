AceCounter <- function(decksize=100, handsize=10, hands=100, trials=1000){
  
  aces <- rep(0,trials)
  
  for(t in 1:trials){
    
    for(step in 1:hands){
    aces[t] <- aces[t] + sum(sample(1:decksize,handsize)==1)
    }
    
  }
  
  hist(aces, xlab = "Number of Aces", main = paste("Aces seen after ", hands," ", handsize , "-card hands (", trials ," trials)" , sep=""))
  
  return(mean(aces))
}

