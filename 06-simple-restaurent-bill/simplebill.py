item = {'pizza': 160.0, 'burger': 100.0, 'coke': 70.0,'fries':100.0 ,'softy': 40.0}
print("MENU")
for i, j in item.items():
    print(i,"-", j)
print()

d1 = {}
ch = 'y'

while ch == 'y':
    n = input('Enter your choice: ').lower()
    cost = item[n]
    print('Cost is:', cost)
    q = int(input('Enter quantity: '))
    amount = cost * q
    print('Amount is:', amount)
    ch = input('Do you want to continue (y/n): ')
    d1[n] = [cost, q, amount]
print(d1)
print("\nITEMNAME    COST   QUANTITY   TOTAL")
print('-'*30)
bill=0
for i, j in d1.items():
    print(i, end="  ")
    bill+=j[2]
    for k in j:
      print(k,end='\t')
    print()
print('-'*30)
print("\nTotal bill is:", bill)
