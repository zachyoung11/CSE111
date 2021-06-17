questions = [
    "1. I feel that I am a person of worth, at least on an equal plane with others. ",
    "2. I feel that I have a number of good qualities. ",
    "3. All in all, I am inclined to feel that I am a failure. ",
    "4. I am able to do things as well as most other people. ",
    "5. I feel I do not have much to be proud of. ",
    "6. I take a positive attitude toward myself. ",
    "7. On the whole, I am satisfied with myself. ",
    "8. I wish I could have more respect for myself. ",
    "9. I certainly feel useless at times. ",
    "10. At times I think I am no good at all. "
]
answers = []


"""
    1, 2, 4, 6, 7
    Strongly Disagree	0
    Disagree	1
    Agree	2
    Strongly Agree	3
    """

"""
    3, 5, 8, 9, 10
    Strongly Disagree	3
    Disagree	2
    Agree	1
    Strongly Agree	0
    """

# Define functions

def main():
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly")
    print("apply to yourself. Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    statement_answers()

    score = scoring()
    print(f"Your score is {score}")
    print("A score below 15 may indicate problematic low self-esteem.")

# Print the 10 statements and return a response from the user
def statement_answers():
    for question in questions:
        # while answer != ["D", "d", "a", "A"]:
        print(question)
        answer = input("Enter D, d, A, or a: ")
        answers.append(answer)

def scoring():
    # for i in answers[0, 1, 3, 5, 6]:
    i = answers[0]    
    if i == "D":
        total = 0
    elif i == "d":
        total = 1
    elif i == "a":
        total = 2
    elif i == "A":
        total = 3
    answers[0] = total

    i = answers[1]    
    if i == "D":
        total = 0
    elif i == "d":
        total = 1
    elif i == "a":
        total = 2
    elif i == "A":
        total = 3
    answers[1] = total

    i = answers[3]    
    if i == "D":
        total = 0
    elif i == "d":
        total = 1
    elif i == "a":
        total = 2
    elif i == "A":
        total = 3
    answers[3] = total

    i = answers[5]    
    if i == "D":
        total = 0
    elif i == "d":
        total = 1
    elif i == "a":
        total = 2
    elif i == "A":
        total = 3
    answers[5] = total

    i = answers[6]    
    if i == "D":
        total = 0
    elif i == "d":
        total = 1
    elif i == "a":
        total = 2
    elif i == "A":
        total = 3
    answers[6] = total
            # answers[i] = total

    positive_answers = answers[0] + answers[1] + answers[3] + answers[5] + answers[6]
    
    # for i in answers[2, 4, 7, 8, 9]:
    i = answers[2]    
    if i == "D":
        total = 3
    elif i == "d":
        total = 2
    elif i == "a":
        total = 1
    elif i == "A":
        total = 0
    answers[2] = total
        
    i = answers[4]    
    if i == "D":
        total = 3
    elif i == "d":
        total = 2
    elif i == "a":
        total = 1
    elif i == "A":
        total = 0
    answers[4] = total

    i = answers[7]    
    if i == "D":
        total = 3
    elif i == "d":
        total = 2
    elif i == "a":
        total = 1
    elif i == "A":
        total = 0
    answers[7] = total

    i = answers[8]    
    if i == "D":
        total = 3
    elif i == "d":
        total = 2
    elif i == "a":
        total = 1
    elif i == "A":
        total = 0
    answers[8] = total

    i = answers[9]    
    if i == "D":
        total = 3
    elif i == "d":
        total = 2
    elif i == "a":
        total = 1
    elif i == "A":
        total = 0
    answers[9] = total
        # answers[i] = total
        
    negative_answers = answers[2] + answers[4] + answers[7] + answers[8] + answers[9]
        
    return positive_answers + negative_answers

main()

