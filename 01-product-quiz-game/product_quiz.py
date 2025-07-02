import random
score=0
print("WELCOME TO PRODUCT OF TWO NUMBERS GAME! LET'S BEGIN")
print()
while score>=0:
 x=random.randint(1,10)
 y=random.randint(1,10)
 print("first number is",x)
 print("second number is",y)
 print()
 res=int(input('enter product of two numbers:'))
 if res==x*y:
  score+=5
  print()
  print("Yay! Right answer, you get 5 points ✅")
  print("Score :",score)
  print()
 else:
  print()
  print('Oops!Wrong answer ❌')
  print('Better luck next time 👍')
  print("You're score is:",score)
  break
