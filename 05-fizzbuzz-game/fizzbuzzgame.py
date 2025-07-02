print("WELCOME TO FIZZBUZZ GAME! LET'S BEGIN")
print("RULES:")
print("1. Type 'x' for next continuing onto next number")
print("2. Type 'fizz' for multiples of 3")
print("3. Type 'buzz' for multiples of 5")
print("4. Type 'fizzbuzz' for multiples of both 3 and 5")
print()
score=0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        a="fizzbuzz"
    elif i % 3 == 0:
        a="fizz"
    elif i % 5 == 0:
        a="buzz"
    else:
        a="x"
    print(f"Number:{i}")
    enter=input("Enter x/fizz/buzz/fizzbuzz:")
    print()

    if enter==a:
      score+=1
      continue
    else:
      print(f"❌Oops! Wrong answer. The answer was {a}")
      break

print("FINAL SCORE:", score)
