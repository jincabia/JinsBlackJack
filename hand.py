import random
class hand:

    def __init__(self,name,score=0):
        self.__name = name
        self.__cards = []
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    def len_of_list(self):
        return len(self.__cards)
    
    def ace_over(self):
        for i in self.__cards:
            self.__score += i

        #changes the value of an ace if the decks score goes over to 21, 11 --> 1
        if 11 in self.__cards and self.__score > 21:
            while self.__score>21:
                index = 0
                while index < len(self.__cards) and self.__score > 21:
                    
                    if self.__cards[index] == 11:
                        self.__cards[index] = 1
                        self.__score = 0
                    index += 1
                for i in self.__cards:
                    self.__score += i

    def draw(self):
        #the deck
        deck = {'2': 2, '3': 3, '4': 4, '5': 5,'6': 6, '7': 7, '8': 8, '9': 9,'10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        
        #draws a card, then takes the name and values
        
        card_name, card_value = random.choice(list(deck.items()))
        print(f"The {self.__name} drew a/an {card_name}")
        
        self.__cards.append(card_value)
        
        self.__score += card_value
        self.__score = 0
        self.ace_over()
        return 

    def __str__(self):
        result = (f"""The {self.__name} score is {self.__score}
---------------------------------------------------------------------------""" "\n")
        if self.__score == 21:
            result = (f"""The {self.__name} has a blackjack
---------------------------------------------------------------------------""" "\n")
        elif self.__score > 21:
            result = (f"""The {self.__name} score is {self.__score} they busted!
---------------------------------------------------------------------------""" "\n")
        return result
        