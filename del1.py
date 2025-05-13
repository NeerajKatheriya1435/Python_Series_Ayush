# list1=[8,9,5,7]

# list1[0]=90
# list1.append(67)
# list1.pop(2)
# list1.sort(reverse=True)
# list2=[9,9,99,999]
# print(list1+list2)
# list1.insert(1,789)
# list1.extend([99,999,99999])
# print(list1)

# tup1=(3,5,8,45,23,4)
# tup1=(1,)
# print(tup1[:3])
# for item in tup1:
#     print(item)

# name="Shubham"
# age=34.987
# # str1="My name is {0} and age is {1}"
# print("My name is",name,"and age is",age)
# # print(str1.format(name,age))
# print("My name is {0} and age is {1}".format(name,age))
# print(f"My name is {name} and age is {age:.1f}")
# print(f"My name is {{hw}} and age is {{}}")

# """
# hello kaise ho
# """

# def addTwo():
#     """
#     This adds two number
#     """
#     print("Hello bab")

# print(addTwo.__doc__)


# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*fact(n-1)

# fact(6)

# print(fact(5))

# sets in python

# set1={5,7,3,2,7,8,9,4}
# set2={5,4,3,8,7}
# set3=set1.union(set2)
# set3=set()
# print(type(set3))
# set4=set1.intersection(set2)
# set1.update(set2)
# set4=set1.symmetric_difference(set2)
# set4=set1.difference(set2)
# set4=set1.isdisjoint(set2)
# set4=set1.issuperset(set2)
# set4=set2.issubset(set1)
# set1.add("Hello")
# set1.remove(7)
# set1.discard(99)
# set1.remove(99)
# set1.clear()
# set1.pop()
# print(set1)

# Dictionaries in python

dict1={
    "name":"Hello",
    "age":78
}
# print(dict1["name1"])
# print(dict1.get("name1"))

# print(type(dict1.keys()))
# print(dict1.values())

# for item in dict1:
#     print(dict1[item])

# for item in dict1.keys():
#     print(dict1[item])

for key,value in dict1.items():
    print(f"{key}:{value}")









