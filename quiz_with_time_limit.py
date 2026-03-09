import time

def ask_question(question, options, correct_answer, time_limit):
    print("\n" + question)
    for option in options:
        print(option)

    print(f"You have {time_limit} seconds to answer!")
    
    start_time = time.time()
    answer = input("Enter your answer (a/b/c/d): ").lower()
    end_time = time.time()

    time_taken = end_time - start_time

    if time_taken > time_limit:
        print(" Time's up! You took too long.")
        return 0
    elif answer == correct_answer:
        print(" Correct!")
        return 1
    else:
        print(f"Wrong! Correct answer is {correct_answer}")
        return 0


def timer_quiz():
    print(" Welcome to the Timer Quiz Game!")
    print("Rules:")
    print("1. You have limited time for each question")
    print("2. Each correct answer = 1 point")
    print("3. If time exceeds, question will be marked wrong\n")

    score = 0
    time_limit = 10  # seconds per question

    # Question 1
    score += ask_question(
        "Q1. What does CPU stand for?",
        ["a) Central Processing Unit", "b) Computer Personal Unit",
         "c) Central Program Utility", "d) Control Processing Unit"],
        "a", time_limit
    )

    # Question 2
    score += ask_question(
        "Q2. Which language is used for web development?",
        ["a) Python", "b) HTML", "c) Java", "d) C++"],
        "b", time_limit
    )

    # Question 3
    score += ask_question(
        "Q3. Which symbol is used for comments in Python?",
        ["a) //", "b) <!-- -->", "c) #", "d) /* */"],
        "c", time_limit
    )

    # Question 4
    score += ask_question(
        "Q4. What is the capital of India?",
        ["a) Mumbai", "b) Delhi", "c) Chennai", "d) Kolkata"],
        "b", time_limit
    )

    # Question 5
    score += ask_question(
        "Q5. Which loop is used when iterations are known?",
        ["a) while loop", "b) for loop", "c) do-while", "d) infinite loop"],
        "b", time_limit
    )

    print("\n Quiz Finished!")
    print(f"Your Final Score: {score}/5")

    if score == 5:
        print(" Excellent! Perfect Score!")
    elif score >= 3:
        print(" Good Performance!")
    else:
        print(" Keep Practicing!")

# Start the timer quiz
timer_quiz()