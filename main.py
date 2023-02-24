from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []


def make_bank(questions):
    for question in questions:
        que = question["question"]
        ans = question["correct_answer"]
        prompt = Question(que, ans)
        question_bank.append(prompt)


make_bank(question_data)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz over!!")
print(f'Your final score was {quiz.score}/{quiz.question_number}')