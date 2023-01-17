class QuizBrain:
  def __init__(self,question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0
  
  def next_question(self):
    current_q = self.question_list[self.question_number]
    self.question_number +=1
    guess = input(f"Q{self.question_number}.) {current_q.question} \n Enter True or False\n").title()
    self.check_answer(guess,current_q.answer)

  def still_has_questions(self):
    return self.question_number < len(self.question_list)
      

  def check_answer(self,user_ans, corr_ans):
    if user_ans.lower() == corr_ans.lower():
      print("Nice")
      self.score+=1
    else:
      print("Wrong")
    print(f"The correct answer is {corr_ans}")
    print(f"Your current socre is: {self.score}/{self.question_number}")
