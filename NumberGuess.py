import random

EASY_LEVEL = 10
HARD_LEVEL = 5
def randomDefining():
    Number = random.randrange(1,100+1)
    return Number
    
def setDifficulty():
    difficulty = input("Chose a difficulty level. Type 'easy' or 'hard': ")
    if difficulty.lower() == "easy":
        return EASY_LEVEL
    elif difficulty.lower() == "hard":
        return HARD_LEVEL
    
def check(guess,ans,turn):
    if guess>ans:
        print("High")
        return turn -1
    elif guess<ans:
        print("Low")
        return turn - 1
    else:
        print(f"You got itt!! .The answer is {ans}.")
        return 0
        
def game():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number from 1 to 100")
    answer = randomDefining()
    print(f"Answer is {answer} ")
    turns = setDifficulty()
    guess = 0
    game_not_finished = True
    while game_not_finished:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input())
        turns = check(guess,answer,turns)
        if turns == 0:
            if guess == answer :
                print("congratsss you won.")
            else:
                print("Game over,you ran out of guesses.") 
                print(f"The correct answer was {answer}")
            
            game_not_finished = False   
        elif guess != answer:
            print("guess again")       
game()


