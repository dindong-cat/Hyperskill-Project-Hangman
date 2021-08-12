import random
print("H A N G M A N")  # Write your code here
x = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(x)
answer_set = set()
wrong_attempt = set()
hidden_answer = "-" * len(answer)
chance = 8

while True:
    decision = input('Type "play" to play the game, "exit" to quit: ')
    if decision == "play":
        while chance > 0:
            print()
            user_input = input(f"{hidden_answer}\nInput a letter: ")
            if len(user_input) != 1:
                print("You should input a single letter")
            elif user_input.isalpha() is False or user_input.islower() is False:
                print("Please enter a lowercase English letter")
            else:
                if user_input in answer:
                    if user_input not in answer_set:
                        answer_set.add(user_input)
                        hidden_answer = ""
                        for i in answer:
                            if i in answer_set:
                                hidden_answer += i
                            else:
                                hidden_answer += "-"
                        if hidden_answer == answer:
                            break
                    else:
                        print("You've already guessed this letter")
                else:
                    if user_input not in wrong_attempt:
                        wrong_attempt.add(user_input)
                        print("That letter doesn't appear in the word")
                        chance -= 1
                    else:
                        print("You've already guessed this letter")

        if hidden_answer == answer:
            print(answer)
            print(f"You guessed the word {answer}!")
            print("You survived!")

        if chance < 1:
            print("You lost!")
            print()

    elif decision == "exit":
        break
