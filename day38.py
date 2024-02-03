a=input("Enter any value between 5 and 9")
if(a.startswith("quit")):
 print("Code ended")
else:
 b=int(a)
 if(b<5 or b>9):
  raise ValueError("Value should be between 5 and 9")
 else:
  print("Corret number entered!")