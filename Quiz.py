
def show_menu():
    print("\n===== QUIZ APPLICATION =====")
    print("1. Start Quiz")
    print("2. View Quiz Instructions")
    print("3. Exit")


def show_instructions():
    print("\n===== QUIZ INSTRUCTIONS =====")
    print("1. Each question has four options.")
    print("2. Enter A, B, C, or D to answer.")
    print("3. Each correct answer earns 1 mark.")
    print("4. There is no negative marking.")
    print("5. Your final score will be displayed.")


def start_quiz():
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. def",
                        "C. define", "D. fun"],
            "answer": "B"
        },
        {
            "question": "Which data type stores key-value pairs in Python?",
            "options": ["A. List", "B. Tuple",
                        "C. Dictionary", "D. Set"],
            "answer": "C"
        },
        {
            "question": "Which symbol starts a comment in Python?",
            "options": ["A. //", "B. #",
                        "C. /*", "D. &"],
            "answer": "B"
        },
        {
            "question": "Which function displays output in Python?",
            "options": ["A. input()", "B. show()",
                        "C. print()", "D. display()"],
            "answer": "C"
        },
        {
            "question": "Which data type represents True or False?",
            "options": ["A. int", "B. str",
                        "C. float", "D. bool"],
            "answer": "D"
        }
    ]

    score = 0
    correct = 0

    print("\n===== EXAMPLE QUESTIONS =====")

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for option in q["options"]:
            print(option)

        while True:
            user_answer = input("Enter your answer: ").strip().upper()
            if user_answer in ("A", "B", "C", "D"):
                break
            print("Invalid choice! Enter A, B, C, or D.")

        if user_answer == q["answer"]:
            print("Correct answer!")
            score += 1
            correct += 1
        else:
            print("Incorrect!")
            print("Correct answer:", q["answer"])

    total = len(questions)
    incorrect = total - correct
    percentage = (score / total) * 100

    print("\n===== QUIZ RESULTS =====")
    print("Total Questions:", total)
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print(f"Final Score: {percentage:.0f}%")

    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good job!")
    else:
        print("Performance: Keep practicing!")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            start_quiz()
        elif choice == "2":
            show_instructions()
        elif choice == "3":
            print("Thank you for using the Quiz Application!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

        if choice in ("1", "2"):
            again = input(
                "\nWould you like to return to the main menu? (yes/no): "
            ).strip().lower()

            if again != "yes":
                print("Thank you for playing!")
                break


if __name__ == "__main__":
    main()
