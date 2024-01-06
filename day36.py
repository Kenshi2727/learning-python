#exception handling
a = input("Enter a sweet and sour number:")
print("Multiplication table of given number is:")

try:
   for i in range(1,11):
      print(f"{int(a)} X {i}={int(a)*i}")

#can handle specific exceptions
except ValueError:
    print("Invalid value entered!")
except Exception as e:
    print("Sorry!The following error occurred:")
    print(e)

print("some lines of code") #error in above line causes this line to cease to execute if error not handled
print("end of code")