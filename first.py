name = input("Enter your name: ")
print("Hello,", name)


age=int(input("Enter your age:"))
print("You are",age,"years old")

price=int(input("Enter a price:"))
print("Final price=",price)


a, b = map(int, input("Enter two numbers: ").split())
print(a + b)

x,y,z=map(int,input("Enter three float numbers:").split())
print(x,y,z)

nums=list(map(int,input("Enter a numbers:").split()))
print(nums)


words = input("Enter words: ").split()
print(words)

data=input("Enter values:").split(",")
print(data)

expr=input("Enter expression:")
result=eval(expr)
print("Result=",result)

age=input("Enter your age:")

if(age>=18):
    print("You can drive the car!")

else:
     print("You cannot drive the car!")


age = int(input("Enter your age: "))
if (age>=18):
    print("You can drive the car!")
else:
    print("You cannot drive the car!")



name=input("Enter name of the student:")
marks=list(map(int,input("Enter the marks:").split()))


average=sum(marks)/len(marks)

print("student name",name)
print("student marks",marks)
print("average marks",average)