import random
def guess():
    player = input("Enter your name: ")
    lower = int(input("Enter the lower limit of the range: "))
    upper = int(input("Enter the upper limit of the range: "))
    rounds = int(input("Enter the number of rounds you want to play: "))
    total = 100
    for round_num in range(1, rounds+1):
        print(f"\nRound {round_num}:\n")
        secret = random.randint(lower, upper)

        while True:
            print(f"Total Points: {total}")
            guess = int(input("Guess the number: "))

            if guess == secret:
                print("Congratulations! You guessed the correct number!")
                break
            elif guess < secret:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
                total -= 5
                if total <= 0:
                  print("Oops! You ran out of points. Game over!")
                return

    print("You have completed all the rounds.")
    print("Total Points: {total_points}")

guess()