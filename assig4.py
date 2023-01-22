#q1
grade = int(input("enter marks"))
if grade < 25:
    print("a")
elif 25 <= grade < 45:
    print("b")
elif 45 <= grade < 50:
    print("c")
elif 50 <= grade < 60:
    print("d")
elif 60 <= grade < 80:
    print("e")
elif 80 <= grade <= 100:
    print("f")

else:
    print("enter valid grade")
#q2
year = int(input("enter the  year"))
if year % 4 == 0 and year % 100 == 0 and year % 400 != 0 or year % 4 != 0 and year % 100 != 0 and year % 400 != 0:
    leap_year = False
else:
    leap_year = True
if leap_year==True:
    print("its a leap year")
else:
    print("its  not a leap year")

    # q3
    import random

    question_count = 0
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    while question_count < 10:
        a = random.choice(list)
        b = random.choice(num)
        print(a, "x", b)
        answer = int(input("enter the answer"))
        if answer == int(a) * int(b):
            print("good one ")
        else:
            print(" I think harder, its", int(a) * int(b))
        question_count += 1