# Ans 1
string = input("Enter a string: ")
words = string.split() if " " in string else list(string)
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)

# Ans 2
import datetime

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
if not (1 <= month <= 12) or not (1 <= day <= 31) or not (1800 <= year <= 2025):
    print("Invalid input date")

else:
    input_date = datetime.datetime(year, month, day)

    next_date = input_date + datetime.timedelta(days=1)

    print("Next date:", next_date.strftime("%Y-%m-%d"))

# Ans 3
result = []
for i in range(1, 11):
    t = (i, i ** 2)
    result.append(t)
print(result)

# Ans 4
grade = int(input("Enter a grade between 4 and 10: "))

if grade < 4 or grade > 10:
    print("Error: grade must be between 4 and 10")
else:
    if grade >= 9:
        letter_grade = "A"
        performance = "Excellent"
    elif grade >= 8:
        letter_grade = "B"
        performance = "Very Good"
    elif grade >= 7:
        letter_grade = "C"
        performance = "Good"
    elif grade >= 6:
        letter_grade = "D"
        performance = "Average"
    else:
        letter_grade = "F"
        performance = "Below Average"

    print("Your Grade is {} and {} performance".format(letter_grade, performance))

# Ans 5
for i in range(10, 0, -1):
    for j in range(11 - i):
        print(" ", end="")
    for k in range(i):
        print(chr(65 + k), end=" ")
    print()

# Ans 6
students = {}

while True:
    name = input("Enter the name of the student: ")
    sid = input("Enter the SID of the student: ")

    students[sid] = name

    more = input("Do you want to add more students (Y/N)? ")
    if more.upper() == 'N':
        break

print("\nStudents' Details:")
for sid, name in students.items():
    print(f"SID: {sid}, Name: {name}")

sorted_students = sorted(students.items(), key=lambda x: x[1])

print("\nSorted Students (by name):")
for sid, name in sorted_students:
    print(f"SID: {sid}, Name: {name}")

sorted_students = sorted(students.items(), key=lambda x: x[0])

print("\nSorted Students (by SID):")
for sid, name in sorted_students:
    print(f"SID: {sid}, Name: {name}")

sid = input("\nEnter the SID of the student you want to search: ")
if sid in students:
    print(f"Name of the student with SID {sid}: {students[sid]}")
else:
    print(f"No student found with SID {sid}")

[2:30 pm, 11/01/2023] Jappan(Ee): set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

#a

a=set1^set2
print(a)

#b

b1=set1-set2-set3
b2=set2-set1-set3
b3=set3-set1-set2
b=b1|b2|b3
print(b)

#c

set_union=set1|set2|set3
c1=set1&set2&set3
c = set_union-b-c1
print(c)

#d

set={1,2,3,4,5,6,7,8,9,10}
print(set-set1)

#e

set={1,2,3,4,5,6,7,8,9,10}
print(set-set1-set2-set3)
[2:31 pm, 11/01/2023] Jappan(Ee): def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms = int(input('Enter the number of terms'))

list1=[]
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i))
       list1.append(fibo(i))
print(sum(list1)/len(list1))