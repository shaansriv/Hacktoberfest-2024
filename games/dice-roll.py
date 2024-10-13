import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def dice_rolling_game():
    print("Welcome to the Dice Rolling Game!")
    
    while True:
        roll = input("\nPress Enter to roll the dice (or type 'exit' to quit): ").lower()
        
        if roll == 'exit':
            print("Thanks for playing!")
            break
        
        dice1, dice2 = roll_dice()
        print(f"You rolled {dice1} and {dice2}. Sum: {dice1 + dice2}")
        
if __name__ == "__main__":
    dice_rolling_game()
