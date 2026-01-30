# ---------------------------------------------
# Assignment-3: Build Your Own Quiz Game
# ---------------------------------------------
def login():
    print("===== STUDENT LOGIN =====")
    student_id = input("Enter Student ID: ")
    password = input("Enter Password: ")

    if student_id == "12345" and password == "python2025":
        print("\nLogin Successful! ✅")
        return True
    else:
        print("\n❌ Login Failed! Incorrect ID or Password.")
        return False

def evaluate_performance(score, total):
    print("\n===== RESULT =====")
    print(f"Your Score: {score}/{total}")

    if score == total:
        print("🌟 Excellent! You are a Python Champ 🏆")
    elif 17 <= score < total:
        print("👍 Very Good! You have strong Python skills.")
    elif 12 <= score < 17:
        print("🙂 Good! But you can improve more.")
    elif 7 <= score < 12:
        print("⚠ Needs Improvement. Keep practicing!")
    else:
        print("❌ Poor performance. Study harder next time!")


# ---------- QUIZ QUESTIONS ----------
questions = [
    {
        "question": "What is the output of: print(type([]))?",
        "options": {
            "a": "<class 'list'>",
            "b": "<class 'dict'>",
            "c": "<class 'set'>",
            "d": "<class 'tuple'>"
        },
        "answer": "a"
    },
    {
        "question": "Which file extension is used for Python files?",
        "options": {"a": ".py", "b": ".pyt", "c": ".python", "d": ".pt"},
        "answer": "a"
    },
    {
        "question": "Which keyword defines a function?",
        "options": {"a": "func", "b": "define", "c": "def", "d": "function"},
        "answer": "c"
    },
    {
        "question": "Which datatype is immutable?",
        "options": {"a": "list", "b": "set", "c": "dict", "d": "tuple"},
        "answer": "d"
    },
    {
        "question": "PEP stands for?",
        "options": {"a": "Python Enhancement Proposal", "b": "Python Efficient Programming",
                    "c": "Programming Enhancement Plan", "d": "None"},
        "answer": "a"
    },
    {
        "question": "Exponentiation operator in Python?",
        "options": {"a": "^", "b": "**", "c": "//", "d": "^^"},
        "answer": "b"
    },
    {
        "question": "Which does NOT allow duplicates?",
        "options": {"a": "list", "b": "dictionary", "c": "set", "d": "tuple"},
        "answer": "c"
    },
    {
        "question": "Method to add element in list?",
        "options": {"a": "add()", "b": "append()", "c": "push()", "d": "insert()"},
        "answer": "b"
    },
    {
        "question": "Output of 10 // 3?",
        "options": {"a": "3", "b": "4", "c": "3.33", "d": "Error"},
        "answer": "a"
    },
    {
        "question": "Keyword for exception handling?",
        "options": {"a": "catch", "b": "except", "c": "exception", "d": "error"},
        "answer": "b"
    },
    {
        "question": "Loop used to iterate a sequence?",
        "options": {"a": "repeat", "b": "foreach", "c": "for", "d": "loop"},
        "answer": "c"
    },
    {
        "question": "Length of 'Python'?",
        "options": {"a": "5", "b": "6", "c": "7", "d": "Error"},
        "answer": "b"
    },
    {
        "question": "Which is a Boolean?",
        "options": {"a": "TRUE", "b": "true", "c": "False", "d": "0"},
        "answer": "c"
    },
    {
        "question": "Symbol for comments?",
        "options": {"a": "//", "b": "#", "c": "/* */", "d": "--"},
        "answer": "b"
    },
    {
        "question": "Stores key-value pairs?",
        "options": {"a": "tuple", "b": "dictionary", "c": "set", "d": "list"},
        "answer": "b"
    },
    {
        "question": "Output of bool(0)?",
        "options": {"a": "True", "b": "False", "c": "0", "d": "1"},
        "answer": "b"
    },
    {
        "question": "Function to get maximum value?",
        "options": {"a": "max()", "b": "maximum()", "c": "top()", "d": "highest()"},
        "answer": "a"
    },
    {
        "question": "Function for user input?",
        "options": {"a": "get()", "b": "scan()", "c": "input()", "d": "read()"},
        "answer": "c"
    },
    {
        "question": "Module for random numbers?",
        "options": {"a": "math", "b": "random", "c": "os", "d": "sys"},
        "answer": "b"
    },
    {
        "question": "Keyword to exit loop?",
        "options": {"a": "stop", "b": "quit", "c": "break", "d": "exit"},
        "answer": "c"
    }
]


# ---------- QUIZ FUNCTION ----------
def start_quiz():
    print("\n🧪 Welcome to the Python Quiz Game!")
    score = 0
    question_number = 1
    total_questions = len(questions)

    for q in questions:
        print(f"\nQuestion {question_number}: {q['question']}")
        for key, value in q["options"].items():
            print(f"{key}) {value}")

        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

        question_number += 1

    # Show final performance summary
    evaluate_performance(score, total_questions)


# ---------- MAIN PROGRAM ----------
if login():
    start_quiz()
else:
    print("Access Denied. Try again!")