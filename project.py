questions = [{"question": "Which symbol is used for comments in Python code cells?","options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],"answer": "B"},
    {   "question": "Which data type is used to store True or False?",   "options": ["A. int", "B. float", "C. bool", "D. string"],"answer": "C" },
    { "question": "Which function is used to display output in python?", "options": ["A. show()", "B. display()", "C. print()", "D. output()"],"answer": "C"},
    {"question": "Which one is string?","options": ["A. (3.14)", "B. 'python'", "C. [true]", "D. false"],"answer": "B"},
    { "question": "Which keyword is used to define a function?","options": ["A. function", "B. define", "C. def", "D. fun"],"answer": "C"},
    {
        "question": "Which collection is ordered and changeable?",
        "options": ["A. Tuple", "B. List", "C. Set", "D. String"],
        "answer": "B"
    },
    {
        "question": "What is the output of 10 // 3?",
        "options": ["A. 3", "B. 3.33", "C. 1", "D. 0"],
        "answer": "A"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. //", "C. **", "D. %%"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used for a condition?",
        "options": ["A. if", "B. when", "C. check", "D. condition"],
        "answer": "A"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. scan()", "B. get()", "C. input()", "D. read()"],
        "answer": "C"
    }
]

def login():
    print("STUDENT LOGIN")
    
    username = input("Enter Username: ")
    Regno = input("Enter Reg.no.: ")
    print("Login successful!")
        
def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def start_quiz():

    score = 0
    a = []

    print("QUIZ STARTED")
    print("Total Questions:10")
    print("Each question carries 1 mark.")
    print("Enter A, B, C or D.")

    for i in questions:
        print(i["question"])
        for option in i["options"]:
            print(option)
        while True:
            answer = input("Your Answer: ").upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid answer! Enter A, B, C or D.")
        a.append(answer)
        if answer == i["answer"]:
            print("Correct!")
            score += 1
        else:
            print(
                "Wrong! Correct answer is",
                i["answer"]
            )

    return score, a

def display_result(score, a):

    total = len(questions)

    percentage = (score / total) * 100

    grade = calculate_grade(percentage)

    print("EXAM RESULT")

    print("Total Questions :", total)
    print("Correct Answers :", score)
    print("Wrong Answers   :", total - score)
    print("Marks Obtained  :", score, "/", total)
    print("Percentage      :", round(percentage, 2), "%")
    print("Grade           :", grade)

    if percentage >= 40:
        print("Result:PASS")
    else:
        print("Result:FAIL")

def review_answers(a):

    print("ANSWER REVIEW")
    
    for i, question in questions(questions):

        correct = question["answer"]
        student = a[i]

        print("Question", i + 1)
        print(question["question"])

        print("Your Answer    :", student)
        print("Correct Answer :", correct)

        if student == correct:
            print("Status : Correct")
        else:
            print("Status : Wrong")

def main():

    print("ONLINE QUIZ / EXAM SYSTEM")
    
login()
while True:
        print(" MENU")
        print("1. Start Exam")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            score, a = start_quiz()
            display_result(score, a)
            print("Thank you")
            break
        elif choice == 2:
            print("Exiting")
            break
        else:
            print("Invalid choice")
main()