"""
Program: average_input_score.py
Author: Kelly Smith
Last date updated: 09/17/2019

Program
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
