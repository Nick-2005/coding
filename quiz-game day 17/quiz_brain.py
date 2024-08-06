class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number <len(self.question_list)

    def check_answer(self,user_answer,correct_annswer):
        if user_answer.lower() == correct_annswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You are wrong")

        print(f"Your current score is {self.score}/{self.question_number}")
        
        


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.Q} (True/False): ")
        self.check_answer(user_answer,current_question.A)