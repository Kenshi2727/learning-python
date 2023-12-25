#understanding tuples in python
tup=(1,2,3,4,5,6,7,8,9)
print(tup,type(tup))
print(tup[8])

if 900990 in tup:
    print("ha")
else:
    print("Na")

tup2=tup[1:9:2]
print("original tuple:",tup)
print("New tuple:",tup2)
