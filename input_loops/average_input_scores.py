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
    print("Welcome! Please complete the following as they appear below.\n")
    first_name = input("First Name: ")
    last_name = input("\nLast Name: ")
    score_input_list = []
    sentinel = -1
    has_input = True


    while (has_input):
      user_input = float(input("\nEnter score for calculation, or -1 to stop: "))
      # print(f'{user_input}' + " " + f'{sentinel}') // Used to verify what is being passed in testing
      # print(score_input_list) // Used to verify what is being passed in testing
      if user_input == sentinel:
        has_input = False
        break
      else:
        score_input_list.append(user_input)
    
    
    average_score = average(score_input_list)


    print(f'{last_name.capitalize()}' + ", " + f'{first_name.capitalize()}' + ": Average Score is " + f'{average_score}')


