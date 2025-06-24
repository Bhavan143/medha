#1.
# def a(*args):
#     c=0
#     for i in args:
#         c+=i
#     print(c)
# a(1,2,3,4,5)

           #or
#1.
# def a(*b):
#     i=0
#     total=0
#     while i<len(b):
#         total+=b[i]
#         i+=1
#     return total
# print(a(1,2,3,4,5))



#2.
# def a(**b):
#     return ",".join(b.keys())
# print(a(name="bhavan",age=19,country="india"))


#3.
# while True:
#     a=input("enter the words:")
#     if a=="exit":
#         break


#4.
# n=0
# while True:
#     print(f"{n}")
#     n+=1
#     if n==5:
#         break
    

#5.
# a=int(input("enter a number:"))
# while True:
#     print(f"the number entered is {a}")
#     break
#     if a<0:
#         continue

#6.
# def maximum(*a):
#     while True:
#         print(max(*a))
#         break
# maximum(1,2,9,20)

#7.
# names = []

# while True:
#     name = input("Enter a name: ")
#     if name == "":
#         break
#     names.append(name)

# print("Names entered:", names)



#8.
# def a(**b):
#     while True:
#         c=b.values()
#         print(f"the total price is:{sum(c)}")
#         break
# a(phone=1000,tv=1000,apple=50)

#9.
# a=1
# b=11
# while a<b:
#     print(a)
#     a+=1
#     if a==5:
#         a+=1
#         continue

#10.
# def valid_age():
#     age=int(input("enter your age:"))
#     while age<0:
#         age=int(input("enter your age:"))
#     print(f"your age is:{age}")

# valid_age()


        



