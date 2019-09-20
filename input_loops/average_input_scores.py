"""
Author: Tyler Hochstetler
The purpose of this assignment is to demonstrate the use of while loops with user input and sentinel value. 
"""

def average(score_list):
  sum = 0
  number_of_scores = len(score_list)


  for score in score_list:
    sum = sum + score
  

  avg_score = sum / number_of_scores


  return avg_score




if __name__ == "__main__":
    pass

