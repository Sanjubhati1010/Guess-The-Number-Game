import random
human_score = 0
computer_score= 0 
print("====   ====   ====       Guess THe Number Game        ===  === === \n\n")

print("Guess a number between 1 and 10 \n")
print("Press Q to exit : ")
import random
human_score = 0
computer_score= 0 
print("====   ====   ====       Guess THe Number Game        ===  === === \n\n")

print("Guess a number between 1 and 10 \n")
print("Press Q to exit : ")

while True:
    user = input("Enter Your Guess (1 to 10 ) or Q to Quit ")
    if user.lower() =="q":
        break
    elif not user.isdigit():
        print("Please eneter a Valid number \n")
        continue
    human_guess = int(user)

    if human_guess < 1 or human_guess > 10:
        print("Please ENter a Number between 1 to 10 \n")
        continue
    human_guess = int(user)

    if human_guess < 1 or human_guess > 10:
        print("Please ENter a Number between 1 to 10 \n")
        continue

    computer_guess= random.randint(1,10)

    print(f"Computer Number  ", {computer_guess})
    print(f"Human Number ", {human_guess})

    if human_guess == computer_guess:
        human_score  += 1 
        print("Correct Human Get 1 Point ")
    else:
        computer_score += 1 
        print("Sorry Human Computer WOn this !!!!!")
    print(f"score -----> Human : {human_score} | Computer : {computer_score}")
    print("-" * 40 )

print("\n ======= Final Score  ======\n")
print(f"Human : {human_score}")
print(f"Computer : {computer_score}")
if human_score > computer_score:
    print(" 🏆 HUMAN WINS ")
elif computer_score > human_score:
    print("💻 Computer WINS")
else:
    print("DRAW")