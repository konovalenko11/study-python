"""
    Exercise 3.3

    Write a program to prompt for a score between 0.0 and 1.0.
    If the score is out of range, print an error message.
    If the score is between 0.0 and 1.0, print a grade using the following table:

    Score Grade
        >=0.9   A
        >=0.8   B
        >=0.7   C
        >=0.6   D
        <0.6    F

    Enter score: 0.95
        A
    Enter score: perfect
        Bad score
    Enter score: 10.0
        Bad score
    Enter score: 0.75
        C
    Enter score: 0.5
        F
"""


def get_grade(xscore):
    if xscore >= 0.9:
        return "A"
    elif xscore >= 0.8:
        return "B"
    elif xscore >= 0.7:
        return "C"
    elif xscore >= 0.6:
        return "D"
    elif xscore >= 0:
        return "F"


# parsing [score] value
while True:
    try:
        score = float(input("Please, enter score:\t"))

        if score < 0 or score > 1:
            raise ValueError("Incorrect score value", score)

        break
    except ValueError as err:
        print("Please, enter numerical value.")
        print(err.args)

grade = get_grade(score)

print("Input score: [%.2f]; Grade: [%s]" % (score, grade))
