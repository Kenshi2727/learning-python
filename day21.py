# #required arguments
# def average(a,b):
#     print("Average of the given two numbers is:",(a+b)/2)
#
#
# average(2,4)
# #default arguments
# def average1(a=9, b=1):
#     print("Average of the given two numbers is:", (a+b)/2,a,b)
#
# # average1()
# # average1(2,4) #overriden 9 and 1
# # average1(1) #a value overriden
# # average1(b=9) #b value overriden
#
# average1(b=90,a=59)
#

#variable lengh=th arguments
# def  average(*numbers):  #argument becomes tuple
#     sum=0
#     print(type(numbers))
#     for i in numbers:
#         sum += i
#     sum /= len(numbers)
#     print("Average of given numbers is:",sum)
#
# average(1,2,3,4,5,6,7,8,9,10)
#
def average(a, b):
    return (a+b)/2


c = average(2, 4)
print("Average of the given two numbers is:", c)
