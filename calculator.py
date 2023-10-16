def add(a,b):
    calculate = a + b
    print(str(a) + ' + ' + str(b)+ " = ", calculate)
          

def sub(a,b):
    calculate = a -b
    print(str(a) + ' - ' + str(b)+ " = ", calculate)

def multi(a,b):
    calculate = a * b
    print(str(a) + ' * ' + str(b)+ " = ", calculate)

def div(a,b):
    calculate = a / b
    print(str(a) + ' / ' + str(b)+ " = ", calculate)


print("A.addition")
print("B.substruction")
print("C.multiplication")
print("D.divition")
print("Exit program")

choice = input("enter your choice : ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    add(a,b) 

elif choice == "b" or choice == "B":
    print("substraction")
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    sub(a,b) 

elif choice == "c" or choice == "C":
    print("multiplication")
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    multi(a,b) 

elif choice == "d" or choice == "D":
    print("divition")
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    div(a,b) 
else:
    print("program exit")
    quit()

