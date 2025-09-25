a =[1,2,3,4,5,6,7,8,9,0]
# print(type(a))
# print(a[-1])
# print(a[0:-1])
# print(a[:])
# print(a[:6])
# print(a[2:6:2])
# print(a[::2])

# def add(a,b):
#     print(a+b)
#     return 0
# add(2,3)

# b="Edunet Foundation  "
# print(b[7:-5])
# print(b)


# for x in b:
#     print(x)

# print(len(b.strip()))

# mylist=["apple","banana","cherry",12.5,True]
# print(mylist)
# print(len(mylist))
# mylist[2]="Anand"
# print(mylist[2])
# print(mylist)
# mylist.append("banana")
# print(mylist)
# mylist.remove(12.5)
# print(mylist)
# mylist.sort()
# print(mylist)

# mytuple=("apple","mango","cherry","pineapple","banana")
# print(mytuple[1])
# myset={
#     "apple","mango","cherry","pineapple","banana","apple"
# }
# print(myset)

# mydict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(mydict["year"])
# mydict["year"]=2020
# print(mydict)

a=int(input("eneter a number:"))
b=int(input("eneter a number:"))
print("the sum is :",a+b)
print("the mul is :",a*b)
print("the sub is :",a-b)
print("the div is :",a/b)

if (a%2==0):
    print("it is even:",a)
else:
    print("it is not even:",a)

for i in range(b):
    print((i+1)*a)
    