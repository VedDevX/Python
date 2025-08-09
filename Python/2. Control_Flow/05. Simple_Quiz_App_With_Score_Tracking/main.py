# Simple Quiz App with Score Tracking

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) London", "C) Paris", "D) Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Leo Tolstoy", "D) Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water at sea level (in Celsius)?",
        "options": ["A) 90", "B) 100", "C) 110", "D) 120"],
        "answer": "B"
    }
]

score = 0  # Initialize score

for item in quiz_questions:
    print(item["question"])  # Print the question
    
    # Print all options
    for option in item["options"]:
        print(option)
    
    # Take user input (convert to uppercase to match answer keys)
    user_answer = input("Enter your answer (A, B, C, D): ").upper()
    
    # Check if the answer is correct
    if user_answer == item["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {item['answer']}.\n")

print(f"Quiz complete! Your total score is {score} out of {len(quiz_questions)}.")

    