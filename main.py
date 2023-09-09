import random
import hand as ingame

BJ_MENU = {1:'Start Game', 2:"Exit"}
IN_GAME_MENU = {1:"Hit", 2:"Stand"}

# menu printing
def print_options(options):
        """
        print_options - method to print out a menu
        Arguments
         - a dictionary representing the menu
        
        Returns 
        - menuOption
        
        
        """
        for key, value in options.items():
            print(f'{key} - {value}')
        return int(input('\nEnter Menu Option: '))
     
     
def determine_winner(user_hand_score,house_hand_score, user_len, house_len):
        
        """
        determine_winner - method to check who the winner is or if it is a draw
        
        Arguments
        - user_hand_score, the users score
        - house_hand_score, the house score
        - user_len - the amount of cards the user has in their deck
        - house_len - the amount of cards the user has in their deck
        

        Returns
        - none

        """



        print(f"The users score is {user_hand_score} and the houses score is {house_hand_score}")
        if user_len == house_len and user_len == 5:
            print("Both players obtained 5 cards")
        else:
            #5 card trick
            if user_len == 5 and user_hand_score <= 21:
                print("User got a Five Card Trick, you win")
                return

            elif house_len == 5 and house_hand_score<= 21:
                print("house got a Five Card Trick, house wins")
                return
     
        #checks if the scores r greater than one another and greater than 21 
        if (user_hand_score > house_hand_score and user_hand_score < 21) or house_hand_score > 21:
            print("User wins \n")
        elif user_hand_score == house_hand_score:
            print("Tie\n")             
        else: 
            print("House wins \n")
     

def play(): 
    gameOption = 0
    user_hand = ingame.hand("User")
    house_hand = ingame.hand("House")
    
    user_hand.draw()
    user_hand.draw()
    print(user_hand)
    house_hand.draw()
    print(house_hand)
    

    #if the user has 21 or 5 cards it will not allow them to draw and if the user decides to stand
    while user_hand.get_score() < 21 and gameOption != 2 and user_hand.len_of_list() < 5:
        gameOption = print_options(IN_GAME_MENU)

        if gameOption == 1:
            user_hand.draw()
            print(user_hand)
            if user_hand.len_of_list() == 5:
                 print("User drew 5 cards and achieved the Five Card Trick\n")
    
    # House keeps drawing until it is greater than the users score or ties with it
    while (house_hand.get_score() < user_hand.get_score() and house_hand.get_score() < 21 and user_hand.get_score() <= 21):
                house_hand.draw()
                print(house_hand)

    #If the user gets a 5 card trick the house keeps drawing to either 21 or 5 cards

    if (house_hand.get_score() > user_hand.get_score() and house_hand.get_score() < 21 and user_hand.get_score() <= 21) and user_hand.len_of_list() ==5:
         while house_hand.len_of_list() < 5 and house_hand.get_score()<21:
              house_hand.draw()
              print(house_hand)

    determine_winner(user_hand.get_score(),house_hand.get_score(),user_hand.len_of_list(),house_hand.len_of_list())

def main():
    startGame = 0
    while startGame != 2:

        if startGame == 1:
             play()
        print("Jins Blacjac")
        startGame = print_options(BJ_MENU)
        print()
    
    print("Thanks for playing")

if __name__ == "__main__":
    main()