#This game is called Blackjack. The goal of blackjack is to get the sum of the
#cards as close to 21, not exceeding 21, but a higher sum than the dealer's cards.
#The dealer will be the computer and the user is the player.


#Gives out two cards each to the dealer and the player(user) from the deck of cards. 
import random
#H = Hearts; D = Diamonds; S = Spades; C = Clubs; 'D' as in Deca, represents 10


deckOfCards = []
playerCards = []
dealerCards = []


#This should get a random card from the remaining deck of cards.
#As soon as a card is given to the dealer or the player it should be removed from the deck.
def getRandomCard():
    cardIndex = random.randint(0,len(deckOfCards)-1)
    selectedCard = deckOfCards[cardIndex]
    deckOfCards.remove(selectedCard)
    return selectedCard
   
def initialCards(pCards, dCards):
    pCards.append(getRandomCard())
    dCards.append(getRandomCard())
    pCards.append(getRandomCard())
    dCards.append(getRandomCard())
    
#I have to add all players cards. Loop through each card and then add them together.
def getCardsTotal(cards):
    totalScore = 0
    for i in range(len(cards)):
        card = cards[i]
        firstChar = card[0]
        if firstChar.isnumeric():
            totalScore = totalScore + int(firstChar)
        else:
            totalScore = totalScore + 10
    return totalScore
    

# Print the cards on the hands of player or dealer
def printCards(listOfCards):
    print(listOfCards)

#############
#############
# Main Program Starts Here:
#############
#############
file = open("deckofcards.txt")

for line in file:
    deckOfCards = line.strip().split()
file.close()
print('checking deck', deckOfCards)

initialCards(playerCards, dealerCards)
print('player cards are: ')
printCards(playerCards)
playInProgress = True
while playInProgress:
    print('Would you like to take an another card? Y/N')
    if input().lower().startswith('y'):
        playerCards.append(getRandomCard())
        printCards(playerCards)
    else:
        playInProgress = False
# Now it's the dealer's turn to take the cards.
print('dealer cards are: ')
printCards(dealerCards)
while getCardsTotal(dealerCards) < 16:
    dealerCards.append(getRandomCard())
    printCards(dealerCards)


# check if the player is busted (total is over 21)
playerScore = getCardsTotal(playerCards)
dealerScore = getCardsTotal(dealerCards)
if dealerScore > 21:
    print('Player wins! The Dealer is busted! The player\'s score is ' + str(playerScore) + ' and the dealer\'s score is ' + str(dealerScore))
elif playerScore > 21:
    print('You are busted!')
elif playerScore > dealerScore:
    print('Player wins! The player\'s score is ' + str(playerScore) + ' and the dealer\'s score is ' + str(dealerScore))
elif playerScore == dealerScore:
    print('It is a draw. The player\'s score is ' + str(playerScore) + ' and the dealer\'s score is ' + str(dealerScore))
else:
    print('Dealer wins! The player\'s score is ' + str(playerScore) + ' and the dealer\'s score is ' + str(dealerScore))

# Go on to delaer cards

#print('Dealer cards are:')
#printCards(dealerCards)

# What Works: The player and dealer are able to get the cards needed to try to win the game. The program automatically calulcates the value of
#their cards' worth and decides the winner. 

# What doesn't work: The player is not able to see the first inital dealer's card when drawing for an additional card for themself. 
