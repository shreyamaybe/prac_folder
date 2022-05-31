guess_no=9
guess_count=0
guess_limit=3

while guess_count<guess_limit:
    guess= int(input("Guess the number: "))
    guess_count+=1

    if guess == guess_no:
        print("You won!")
        break
print("Sorry no more chances left:(")