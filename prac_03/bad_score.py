"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    def scores(score):
        if score < 0 or score > 100:
            score_answer = "Invalid score"
        elif score > 90:
            score_answer = "passable"
        elif score > 50:
            score_answer = "excellent!"
        else:
            score_answer = "bad"
        return score_answer

    score = float(input("Enter score: "))
    scores(score)






main()
