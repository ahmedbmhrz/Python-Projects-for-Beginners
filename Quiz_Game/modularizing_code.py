import random
from termcolor import cprint

QUESTIONS = "questions"
OPTIONS = "options"
ANSWER = "answer"


def ask_question(index, question, opetions):
        print(f"Question {index}: {question}")
        for opetion in opetions:
            print(opetion)

        answer = input("your answer:").upper().strip()
        return answer

def run_quiz(quiz):
        random.shuffle(quiz)
        secore = 0
        for index, item in enumerate(quiz, 1):
            answer = ask_question(index, item[QUESTIONS], item[OPTIONS])

            if answer == item[ANSWER]:
                cprint("correct!", "green")
                secore += 1
            else:
                cprint(f"incorrect, the correct answer is {item[ANSWER]}", "red")

            print("----------------------")

            print("quiz over!")
            print(f"your score is {secore} out of {len(quiz)}")

def main():

        quiz = [
            {
                QUESTIONS: "what is the capital of France?",
                OPTIONS: ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
                ANSWER: "A",
            },
            {
                QUESTIONS: "5+2+1-2(2+5)",
                OPTIONS: ["A. 22", "B. 6", "C. 5", "D. -6"],
                ANSWER: "D",
            },
            {
                QUESTIONS: "what is the largest planet in our solar system?",
                OPTIONS: ["A. mars ", "B. Saturn", "C. Jupiter", "D. Earth"],
                ANSWER: "C",
            },
        ]
        run_quiz(quiz)

if __name__ == "__main__":
 main()


