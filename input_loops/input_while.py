"""
Program: input_while.py
Author: Kelly Smith
Last date updated: 09/21/2019

Program to find the average of a list of scores using a while loop
"""
scores =[]
    score = (float(input("Enter a score or -1 to exit ")))
    while score > 0:
        scores.append(score)
        score = (float(input("Enter a score or -1 to exit ")))
