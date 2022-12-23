#ques1
name='Python is a case sensitive language'

#a
print(len(name))

#b
print(name[::-1])

#c
print(name[10:26])

#d
newname=name.replace("a case sensitive","object oriented")
print(newname)

#e
x=name.index("a")
print(x)

#f
y=name.replace(" ","")
print(y)
y1=newname.replace(" ","")
print(y1)

#ques2
a = "Lakshay"
b = "22104054"
c = "Electrical"
d = '10'
print(f" Hey,{a} Here!\n",f"My SID is:{b}\n",f"I am from {c} department and my cgpa is {d}")

#ques3
a = int(56)
b = int(10)

#1
i=a&b
print(i)

#2
j = a|b
print(j)

#3
k=a^b
print(k)

#4
l=a<<2
m=b<<2
print(l)
print(m)

#5
n=a>>2
p=b>>4
print👎
print(p)

#ques4
a = int(input('enter first no :\n'))
b = int(input('enter second number:\n'))
c = int(input('enter third number:\n'))
if b>c:
    if a>b:
…