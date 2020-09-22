import random
win_number=random.randint(1,100)

game_over=False
guess_time=1

guess_number=int(input("gues the number between 1 to 100::\n"))

while not game_over:
    if guess_number==win_number:
        print(f"you are win ,you guessing {guess_time} times ")
        game_over = True

    else:
        
        if guess_number<win_number:
            print("too low")
            guess_time+=1
            guess_number=int(input("you guess again::\n"))
        else:
            print("too high")
            guess_time+=1
            guess_number=int(input("you guess again::\n"))
