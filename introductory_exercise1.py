"""
Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
"""
n1=int(input("enter the first number\n"))
choice=int(input("enter operator of your choice\n, 1.(+), 2. (-), 3.(*), 4.(/), 5.(//), 6.(%)"))
n2=int(input("enter the second number\n"))
if choice==1:
    print(n1+n2)
elif choice==2:
    print(n1-n2)    
elif choice==3:
    print(n1*n2)
elif choice==4:
    print(n1/n2)
elif choice==5:
    print(n1//n2)
elif choice==6:
    print(n1%n2)
else:
    print("none")