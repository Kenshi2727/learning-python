# learning dictionaries in python
dic = {
    1: "Kenshi",
    2: "shinzo",
    3: "Modi",
    4: "Meloni",
    5: "Melodi,daughter of Modi and Meloni",
    6: "fellow citizen of Italy, the homeland of uncle Gandhi"

}
print(dic[5])# throws error if key not present!
print(dic.get(51))

print(dic.keys())
print(dic.values())
for val in dic.values():
    print(val)

for key in dic.keys():
    print(dic[key])

