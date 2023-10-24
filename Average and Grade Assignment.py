#Ludrianna Bazile
#CS 175
#Average and Grade Assignment
responce = "yes"

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5)/5
    return average
     
def determine_grade(score):
    if 90<=score<=100:
        letter_grade="A"
    elif 80<=score<=89:
        letter_grade="B"
    elif 70<=score<=79:
        letter_grade="C"
    elif 60<=score<=69:
        letter_grade="D"
    else:
        letter_grade="F"
    return letter_grade


def repeat(responce):
    while responce =='yes':
        score1 = float(input("Enter score 1: "))
        score2 = float(input("Enter score 2: "))
        score3 = float(input("Enter score 3: "))
        score4 = float(input("Enter score 4: "))
        score5 = float(input("Enter score 5: "))

        print("\n")

        print("Score	    Numeric Grade          Letter Grade")
        print("----------------------------------------------------")
        print("score1        ", score1,"                 ", determine_grade(score1))
        print("score2        ", score2,"                 ", determine_grade(score2))
        print("score3        ", score3,"                 ", determine_grade(score3))
        print("score4        ", score4,"                 ", determine_grade(score4))
        print("score5        ", score5,"                 ", determine_grade(score5))

        print("\n")

        print("Average score: ",calc_average(score1, score2, score3, score4, score5))

        print("\n")

        responce = input("Enter 'yes' if you would like to do another calculation: ")

   

score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
score4 = float(input("Enter score 4: "))
score5 = float(input("Enter score 5: "))

print("\n")

print("Score	    Numeric Grade          Letter Grade")
print("----------------------------------------------------")
print("score1        ", score1,"                 ", determine_grade(score1))
print("score2        ", score2,"                 ", determine_grade(score2))
print("score3        ", score3,"                 ", determine_grade(score3))
print("score4        ", score4,"                 ", determine_grade(score4))
print("score5        ", score5,"                 ", determine_grade(score5))

print("\n")

print("Average score: ",calc_average(score1, score2, score3, score4, score5))

print("\n")

responce = input("Enter 'yes' if you would like to do another calculation: ")

repeat(responce)

