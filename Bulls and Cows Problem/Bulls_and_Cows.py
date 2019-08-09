import random

code = random.sample(range(0, 9), 4)
cows = 0
bulls = 0
score = 0

print("Welcome to Cows and Bulls.\n")

while cows < 4:

    cows = 0
    bulls = 0

    guess_input = input("\nEnter four numbers: ")
    guess_list = list(guess_input)
    guess = list(map(int, guess_list))

    while len(guess) < 4 or len(guess) > 4:
        print("\nThat guess is invalid!")
        guess_input = input("\nEnter four numbers: ")
        guess_list = list(guess_input)
        guess = list(map(int, guess_list))

    for i in range(len(code)):
        if guess[i] in code and guess[i] != code[i]:
            bulls += 1
        if guess[i] in code and guess[i] == code[i]:
            cows += 1

    print("\nCows:  ", cows)
    print("Bulls: ", bulls)
    score += 1

print("Congratulations! The code was", *code)
print("You took ", score, " attempts to crack the code")