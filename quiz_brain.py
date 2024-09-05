
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    current_score = 0
    def next_question(self):
        current_question = self.question_list[self .question_number]
        self.question_number +=1 
        user_answer = input(f"Q. {self.question_number}: {current_question.text}.(True / False)?:")
        answer_text = current_question.answer

        if user_answer == answer_text:
            current_score = self.question_number + 1
            final_score = current_score
            print("You are right")
            print(f"your score is {final_score}/10")
            self.still_has_questions()
        else:
            current_score = self.question_number - 1
            final_score = current_score
            self.question_number = 13
            self.still_has_questions()
            print(f"your score is {final_score}/10")


    def still_has_questions(self):
        if self.question_number > 12:
            print("End of quiz")

        else:
            QuizBrain.next_question(self)


