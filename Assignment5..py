# q1
string = input("enter yours string")
print(string[::-1])


# q2
hey = int(input("enter the range"))
divisible_by = int(input("enter the number ,for divisibility test"))
for i in range(1, hey + 1):
    if i % divisible_by == 0:
        print(i)

# q3
import math
 A = float(input("enter the  your first length"))
B = float(input("enter the your second length"))
C = float(input("enter the your third length"))
if A > B + C or B > A + C or C > A + B:
    triangle = False
    print("triangle cannot be formed")
else:
    triangle = True
    print("triangle can be formed")
if triangle == True:
    semi_perimeter = (A+ B + C)/2
    x = semi_perimeter - A
    y = semi_perimeter - B
    z = semi_perimeter - C
    area = math.sqrt(semi_perimeter*x*y*z)
    print(area)
else:
    print("triangle not formed, area does not exist")

# q4
A = int(input("number of max stars in a line"))
X = 0
while X != A:
    print(X*" * ")
    X += 1
while A != 0:
    print(A*" * ")
    A -= 1

#5

for i in range(65,70):
    k=i
    # Inner loop
    for j in range(65,i+1):
        print(chr(k),end="")
        k=k+1
    print()









# q6
upper_value = int(input("enter the range"))
print("Prime Numbers is not in  range", upper_value, "are: ")
for number in range(2, upper_value + 1):
    for i in range(2, number):
        if (number % i) == 0:
            break
    else:
        print(number)

# q7
x = int(input("enter the range"))
for i in range(1, x+1):
    if i % 7 == 0 and i % 11 == 0:

        print(i)

# q8
initial = []
even = []
odd = []
positive = []
negative = []

while True:
    num = input("enter num")
    if num == '':
        break
    else:
        initial.append(num)
a = 0
while a in range(0, len(initial)):
    if int(initial[a]) % 2 == 0 and int(initial[a]) > 0:
        even.append(initial[a])
        a += 1
    elif int(initial[a]) % 2 != 0 and int(initial[a]) > 0:
        odd.append(initial[a])
        a += 1
    else:
        a += 1
t = 0
while t in range(0, len(initial)):
    if int(initial[t]) < 0:
        negative.append(initial[t])
        t += 1
    else:
        positive.append(initial[t])
        t += 1
h = 0
new = [*set(initial)]
while h < len(new):
    g = new[h]
    p = initial.count(g)
    print(g, "appears", p, "times")
    h += 1

print("even numbers are:-", even)
print("odd numbers are:-", odd)
print("positive numbers are:-", positive)
print("negative numbers are:-", negative)

# q9
string = input("enter your string")
new_string = string.split()
new_new_string = [*set(new_string)]
h = 0
while h < len(new_new_string):
    g = new_new_string[h]
    p = new_string.count(g)
    print(g, "appears", p, "times")
    h += 1
