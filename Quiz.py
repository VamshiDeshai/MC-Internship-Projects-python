def display_question(question, options):
    print(question)
    # print the question
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_user_input(options):
    while True:
        try:
            user_choice = int(input("Enter the number of your answer: "))
            if 1 <= user_choice <= len(options):
                return user_choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def evaluate_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def quiz(questions):
    score = 0
    for question, options, correct_answer in questions:
        display_question(question, options)
        user_choice = get_user_input(options)
        selected_answer = options[user_choice - 1]
        
        if evaluate_answer(selected_answer, correct_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}\n")
    
    return score, len(questions)

def main():
    questions = [
        ("Who is the captain of Chennai Super Kings?",
         ["Hardik Pandya", "M.S Dhoni", "Virat Kohli", "Rohith"],
         "M.S Dhoni"),
        ("When did India win its first ODI World Cup?",
         ["1983", "2007", "2011", "2024"],
         "1983"),
        ("Who is the captain of the Indian team for T20 World Cup 2024?",
         ["Rohith Sharma", "Virat Kohli", "Hardik Pandya", "Surya Kumar Yadav"],
         "Rohith Sharma")
    ]

    print("Welcome to the Quiz!")
    print("Each question has multiple-choice options. Enter the corresponding option number to answer.")
    print("Let's begin!\n")

    score, total_questions = quiz(questions)

    print("\nQuiz finished!")
    print(f"Your final score is: {score} out of {total_questions}")

if __name__ == "__main__":
    main()
