import random
print("WELCOME TO GUESSING GAME! LET'S BEGIN")
print()
secret_num=random.randint(1,100)
ch="y"
while ch=="y":
  secret_num=random.randint(1,100)

  for attempt in range(1,8):
   guess=int(input("Enter your guess: "))

   if guess>secret_num:
     print("Oops, your guess is bigger than the secret number!📉")
   elif guess<secret_num:
     print("Oops, your guess is smaller than the secret number!📈")
   elif guess==secret_num:
     print("YAYY! YOU'RE A BORN GUESSER ⭐")
     break
   else:
     print("Please guess number in range 1-100")

  else:
   print(f"❌ Sorry! You've used all your attempts. The number was {secret_num}")
  print()
  ch=input("Play again?(y/n):") 

print("GAME ENDED")
