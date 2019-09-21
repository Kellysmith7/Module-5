"""
Program: average_input_score.py
Author: Kelly Smith
Last date updated: 09/21/2019

Program to find the average of a list of scores using a while loop
"""


def average():
    scores =[]
    score = (float(input("Enter a score or -1 to exit ")))
    while score > 0:
        scores.append(score)
        score = (float(input("Enter a score or -1 to exit ")))
    return sum(scores) / len(scores)


if __name__ == '__main__':
    first_name = input("Please enter first name ")
    last_name = input("Please enter last name ")
    age = input("Please enter age ")
    print(last_name + ", " + first_name + " " + "Age: " + age + " " + "Average Score: % 5.2f" % average())


  #Tests
  #Kelly Smith 38 90 80 100 -1
  #Result: Smith, Kelly Age: 38 Average Score: 90
  # k l 8 90 85 95 -1
  #Results: l,k Age: 8 Average Score: 90

