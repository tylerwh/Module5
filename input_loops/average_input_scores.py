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


    print(f'{last_name.capitalize()}' + ", " + f'{first_name.capitalize()}' + ": Average Score is {:0.2f}".format(average_score))
    

    # Playing around with formatting average_score
    # score_input_list = [91.1, 86.6, 80.5]
    # average_score = average(score_input_list)
    # print("Average: {:0.2f}".format(average_score))


    #     Input         Expected Output   Actual Output
    #  [90, 90, 90]          90.00            90.00    
    #
    # [95.5, 85.4, 75.3]     85.40            85.40
    #
    # [65.67, 90.1, 45.9,
    # 98.8, 70, 61.5]      71.99/72.00        71.99
    #
    #[87.77, 76.65, 65,
    # 100, 56.7]              77.22           77.22
    #
    #    [0, 0, 0]             0.00            0.00
    #
    # [96.654321, 95]         95.83           95.83           



