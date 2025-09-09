import time
card = input("Plzz Insert  UPI Card \n for inserting card Enter 1 or Enter").lower()
balance = 100000
ATM = 0
if card == "enter"or card == "1":
  print("Thank you for inserting  card \n")
else:
  print("Plzz insert your card \n")
pin = int(input("Enter Your PIN" ))
if pin == 1234:
  print("Enter Your pin is correct \n")
else:
  print("Plzz Enter Your pin correctly")
op = input("Plzz select option \n 1.check balance \n 2.withdraw \n 3.deposite \n select your option ").lower()
if op == "Check balance" or op == "1" :
  print(f"Ok Checking your balance plzz wait")
  print(f"Current balance is {balance}$")
elif op == "Withdraw" or op == "2" :
  a = int(input("Plzz Enter your amount \n maximum withdraw amount is 10000$"))
  if a >=100 and a <= 10000:
    print("Plzz wait...........")
    time.sleep(2)
  if balance >= a:
    print(f"Ok Collect your amount {a} $")
    balance = balance-a
    balance = balance-1
    ATM = ATM + 1
    print(f"Current balance is {balance} $ \n thank you,     visit again")
  else:
    print("You do not have inaf balance")
elif op == "deposite" or op == "3":
  d = int(input("Enter your amount"))
  balance = balance + d
  print(f"Your current balance {balance}$ \n Thank you, Visit again")
else:
  print("Something wrong")