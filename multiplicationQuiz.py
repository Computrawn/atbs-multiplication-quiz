# Python3
# multiplicationQuiz — An exercise in validating user input. See project_details.txt for details.

import random, time


numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # random numbers 0-9
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    # time keeper
    start_time = time.time()
    prompt = f'{questionNumber + 1}: {num1} * {num2} = '
    response = input(prompt)
    end_time = time.time() - start_time
    # number of tries
    tries = 0
    # main loop
    if end_time < 8:
        while int(response) != num1 * num2:
            if tries < 2:
                print("Incorrect. Try again: ")
                response = input(prompt)
                tries += 1
            else:
                print("Limit exceeded.")
                break
        else:
            print(f"Correct!")
            correctAnswers += 1
            time.sleep(1)
    else:
        print('Timed Out.')
    print(end_time)


print(f'{correctAnswers} of {numberOfQuestions} answered correctly.')
