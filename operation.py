

print("what operation do you want?:")
operator=input("enter either +, -, * or divide:")
n1=float(input("enter first number:"))
n2=float(input("enter the secons number:"))
if operator=="+":
    print(n1,operator,n2,"=,n1+n2")
elif operator=='-':
    print(n1,operator,n2,'=',n1-n2)
elif operator=="*":
    print(n1,operator,n2,'=',n1*n2)
elif operator=='/':
    print(n1,operator,n2,'=',n1/n2)
else:
    print("invalid operator")