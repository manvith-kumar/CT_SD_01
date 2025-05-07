# CT_SD_01 - Advanced Text-Based Quiz Game
import time
from random import shuffle

class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "What is the time complexity of a Python dictionary lookup?",
                "options": ["A) O(1)", "B) O(n)", "C) O(log n)", "D) O(n^2)"],
                "answer": "A"
            },
            {
                "question": "Which of these is NOT a Python mutable data type?",
                "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
                "answer": "D"
            },
            {
                "question": "What does PEP 8 refer to in Python?",
                "options": ["A) Python Enhancement Proposal", "B) Python Error Protocol", 
                            "C) Python Execution Plan", "D) Python Extension Package"],
                "answer": "A"
            }
        ]
        shuffle(self.questions)  # Randomize question order

    def display_instructions(self):
        print("""
        ===== PYTHON MASTERY QUIZ =====
        * Answer multiple-choice questions (A/B/C/D)
        * Each correct answer: +10 points
        * No negative marking
        * Type 'quit' to exit early
        """)
        input("Press ENTER to start...\n")

    def run_quiz(self):
        for q in self.questions:
            print(f"\n{q['question']}")
            for option in q["options"]:
                print(f"  {option}")
            
            while True:
                user_input = input("\nYour answer (A/B/C/D): ").upper().strip()
                if user_input == "QUIT":
                    print(f"\nGame ended early! Final score: {self.score}")
                    return
                elif user_input in ("A", "B", "C", "D"):
                    if user_input == q["answer"]:
                        self.score += 10
                        print("✅ Correct! +10 points")
                    else:
                        print(f"❌ Wrong! Correct answer: {q['answer']}")
                    break
                else:
                    print("⚠ Invalid input! Please enter A/B/C/D")

        print(f"\nQuiz completed! Final score: {self.score}/30")

if __name__ == "__main__":
    game = QuizGame()
    game.display_instructions()
    game.run_quiz()