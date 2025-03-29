class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {question.text} (True/False): ").lower()
        self.question_number+=1
        self.check_Answer(user_answer, question.answer)
        # print(f"Q.{self.question_number}: {question.text} Answer is: {question.answer}")
    def check_Answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("you're correct!")
            self.score+=1
        else:
            print("wrong answer")
        print(f"correct answer is: {correct_ans}")
        print(f"your score is {self.score}/{self.question_number}\n")
