print("USE THIS CALCULATOR TO PERFORM BASIC CALCULATIONS! LET'S BEGIN")
print()
a=float(input("enter number:"))
b=float(input("enter number:"))
ch=input("enter symbol:")
if ch=='+':
  c=a+b
  print('sum',c)
elif ch=="-":
  c=a-b
  print('difference',c)
elif ch=="*":
  c=a*b
  print('product',c)
elif ch=="/":
  c=a/b
  print('division',c)
else:
  print("sorry! operation not available")

print()
ch1=input("Do you want to continue? (y/n): ")
while ch1=='y':
  print()
  d=float(input("enter next number:"))
  ch = input("Enter symbol")
  if ch == '+':
        c = c + d
        print("Result:", c)
  elif ch == '-':
        c = c - d
        print("Result:", c)
  elif ch == '*':
        c = c * d
        print("Result:", c)
  elif ch == '/':
        c = c / d
        print("Result:", c)
  else:
        print("Sorry! Operation not available")
  print()
  ch1 = input("Do you want to continue? (y/n): ")
print()
print("final answer is:",c)
