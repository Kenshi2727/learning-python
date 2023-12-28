#set methods
s1={1,2,3,3,4,5}
s2={4,9,5,6,5,6,7,7,8}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

print("Intersection of s1 and s2 is",s1.intersection(s2))
# s1.intersection_update(s2)
# print("Updating s1:",s1)

print("Symmetric Difference of s1 and s2 is", s1.symmetric_difference(s2))

print("Difference of s1 and s2 is",s2.difference(s1))
# s1.difference_update(s2)

print("Checking if s1 is subset of s2:",s1.issubset(s2))
print("Checking if s1 is superset of s2:",s1.issuperset(s2))

s1.add("Helsinki")
print(s1)

# s1.discard("Helsinki") on this line we cannot use this method because below method will give an error if the element is not present in the set
s1.remove("Helsinki")
s1.discard("Helsinki")
print(s1)
# del s1 #this will delete the set
print(s1.pop())

info={'Carla',19,'Helsinki',19,'Balaganj'}

if 'Carla' in info:
    print('Carla Found')
else:
    print('Not Found')

info.clear()
print(info)