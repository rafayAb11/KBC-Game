print("Welcome to Who Wants to Be a Millionaire!")

questions = ["What is the population of the USA?", 
             "Who is the fastest human recorded?", 
             "Who won the 2018 FIFA World Cup?"]

option1 = ["A: 380 million", "B: 400 million", "C: 340 million", "D: 300 million"]
option2 = ["A: Usain Bolt", "B: Trayvon Bromell", "C: Fred Kerley", "D: Asafa Powell"]
option3 = ["A: Portugal", "B: Argentina", "C: France", "D: Croatia"]

print("\nQ1:", questions[0])
print("Options:", option1)

answer1 = input("Answer: ").strip().upper()

if answer1 == 'C':
    print("Correct answer!! You win 250,000")
    choice = input("Do you want to continue? (Y/N): ").strip().upper()

    if choice == 'Y':
        print("\nQ2:", questions[1])
        print("Options:", option2)

        answer2 = input("Answer: ").strip().upper()

        if answer2 == 'A':
            print("Correct answer!! You win 500,000")
            choice2 = input("Do you want to continue? (Y/N): ").strip().upper()

            if choice2 == 'Y':
                print("\nQ3:", questions[2])
                print("Options:", option3)

                answer3 = input("Answer: ").strip().upper()

                if answer3 == 'C':
                    print("Correct answer!! You win 1,000,000\nThanks for playing!")
                else:
                    print("Wrong answer!! You win 250,000")
            else:
                print("Thank you for playing! You win 500,000")
        else:
            print("Wrong answer!! You win 100,000")
    else: 
        print("Thank you for playing! You win 250,000")
else:
    print("Wrong answer!! Thank you for playing")
