from random import randint 
from beautifultable import BeautifulTable

def computer_guess(x):
    low = 1
    high = x
    count = 0
    feedback = ""
    print(f"\n--Please choose a number between 1 and {x} in your mind--")
    while feedback != "c":
        if low != high:
            guess_computer = randint(low , high)
        else:
            guess_computer = low 

        feedback = input(f"\nIs your number {guess_computer} ? Too High(H) , Too Low(L) , Correct(C): ").lower()
        count += 1
        table = BeautifulTable()

        if feedback == "l":
            low = guess_computer + 1
        elif feedback == "h":
            high = guess_computer - 1

    table.set_style(BeautifulTable.STYLE_BOX_ROUNDED) 
    table.rows.append([f"--The computer guess your Number {guess_computer} correctly, in {count} times--"])        
    table.columns.header = ["Computer Win"]
    print(table)

computer_guess(10)        


# Made By Yasin Rezvani