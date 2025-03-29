from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(d["question"],d["correct_answer"]) for d in question_data]
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("you've completed the questions!")
print(f"you scored {quiz.score}/{len(question_bank)}")