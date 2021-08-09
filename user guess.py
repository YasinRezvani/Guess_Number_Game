from random import randint
from beautifultable import BeautifulTable

def guess_user(x):
    low = 1
    high = x
    user_guess = 0 
    random_num = randint(low,high)
    count = 0

    while user_guess != random_num:
        table = BeautifulTable()
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        count += 1
        if random_num > user_guess:
            print("--Guess again, Too low--")
        elif random_num < user_guess:
            print("--Guess again, Too high--")
            
    table.rows.append([f"--You have guessed the number {random_num} correctly in {count} times"])
    table.columns.header = ["You win"]
    print(table)

guess_user(10)

# Made By Yasin Rezvani