# Python3
# multiplicationQuiz — An exercise in validating user input. For more info, see project_details.txt.

import random
import time

correctAnswers = 0

while True:
    numberOfQuestions = input("How many questions do you want to answer?\n")
    try:
        numberOfQuestions = int(numberOfQuestions)
    except ValueError:
        print("Please input integer value.")
        continue
    if numberOfQuestions < 1:
        print("Please enter a positive number.")
        continue
    break

# main loop
for questionNumber in range(numberOfQuestions):
    # random numbers 0-9
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    # timer start
    start_time = time.time()
    prompt = f"{questionNumber + 1}: {num1} * {num2} = "
    response = input(prompt)
    # number of tries
    tries = 0
    # integer and answer validation loop
    while True:
        try:
            response = int(response)
        except ValueError:
            print("Please enter integer value.")
        if response != num1 * num2 and tries < 2:
            print("Incorrect. Try again: ")
            response = input(prompt)
            tries += 1
        else:
            break
    # timer end
    end_time = time.time() - start_time
    # limit validation loop
    if end_time < 8 and response == num1 * num2:
        print(f"Correct. Question answered in {end_time:.2f} seconds")
        correctAnswers += 1
    elif end_time < 8 and response != num1 * num2:
        print("Incorrect. Number of tries exceeded.")
    else:
        print(
            f"Time limit exceeded. It took you {end_time:.2f} seconds to answer the question."
        )
    time.sleep(1)

print(f"Final score: {correctAnswers / numberOfQuestions * 100:.0f}")
