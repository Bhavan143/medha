
# import math
# C=40
# H=20
# D=input("enter comma-seperated input:").split(",")
# for i in D:
#     Q = math.sqrt((4 * C * int(i))/H)
#     print(round(Q))

# rows=int(input("enter the number of rows:"))
# cols=int(input("enter the number of rows:"))
# for i in rows:
#     for j in cols:
#         print(i**2+j**2)

# rows = int(input("Enter the number of rows (X): "))
# cols = int(input("Enter the number of columns (Y): "))
# result = [[i**2 + j**2 for j in range(cols)] for i in range(rows)]
# for row in result:
#     print(row)


# a=input("enter binary numbers:").split(",")
# for i in a:
#     b=int(i,2)
#     if b%7==0:
#         print(i)


# transactions=input("enter the transactions:").split(",")
# balance=0
# for i in transactions:
#     for j in i:
#         c=j.upper()
#         if c.isalpha()=="D":
#             balance=balance+int(i)
#         elif c.isalpha()=="W":
#             balance=balance-int(i)
# print(balance)



# import math
# x,y=0,0
# up=int(input("up:"))
# down=int(input("down:"))
# left=int(input("left:"))
# right=int(input("right:"))
# if up:
#     y+=up
# if down:
#     y-=down
# if right:
#     x+=right
# if left:
#     x-=left
# print(f"expected output:{round(((x**2)+(y**2))**0.5)}")


# from collections import Counter
# a=input("enter the sentence:").split()
# b=Counter(a)
# for i in sorted(b):
#     print(f"{i}:{b[i]}")



# from collections import Counter
# import string
# text = input("Enter the sentence: ").lower()
# text = text.translate(str.maketrans('', '', string.punctuation))
# words = text.split()
# word_counts = Counter(words)
# for word in sorted(word_counts):
#     print(f"{word}: {word_counts[word]}")



# emp=[]
# while True:
#     employee_name=input("enter the name:")
#     if employee_name=="":
#         break
#     years_experience=int(input("enter years of exp:"))
#     salary=int(input("amount:"))
#     details=(employee_name,years_experience,salary)
#     emp.append(details)
# print(sorted(emp))
    
# a=int(input("enter the number:"))
# class generator:
#     def __init__(self,n):
#         self.n=n
#     def b(self):
#         for i in range(0,self.n):
#             if i%3==0 and i%9!=0:
#                 yield i
# gen = generator(a)
# for num in gen.b():
#     print(num)

# n=int(input("enter the number:"))
# a=[i*i-1 for i in range(0,n) ]
# for i in a:
#     if i>1000:
#         print(i)

# import math
# n = int(input("Enter a number: "))
# factorials = [math.factorial(i) for i in range(n + 1) if math.factorial(i) <= 1000]
# print(factorials)

        
# a=int(input("enter the number:"))
# class generator:
#     def __init__(self,n):
#         self.n=n
#     def b(self):
#         for i in range(0,self.n):
#             if i%4==0 and i%6==0:
#                 yield i
# gen=generator(a)
# for num in gen.b():
#     print(num)