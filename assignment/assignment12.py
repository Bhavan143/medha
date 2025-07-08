
# import requests
# print("***RHYMING WORD GENERATOR*****")
# a=input("enter a sentence:")
# endpoint = f"https://api.datamuse.com/words?ml={a}"
# response = requests.get(endpoint)
# data = response.json()
# if response.status_code == 200:
#     for item in data:
#         print(item.get('tags'))


# import requests
# print("***RHYMING WORD GENERATOR*****")
# a=input("enter a sentence:")
# endpoint = f"https://api.datamuse.com/words?rel_jjb={a}"
# response = requests.get(endpoint)
# data = response.json()
# if response.status_code == 200:
#     for item in data:
#         if item.get('score')>950:
#             print(f"{item.get('word')} score:{item.get('score')}")


# a=3
# b=4
# c=a
# a=b
# b=c
# print(a)
# print(b)

# name=input("enter your name:")
# age=input("enter your age:")
# city=input("enter your city:")
# print(f"{name} of age:{age}yrs is from {city}")

# a=[5,4,3,2,6]
# # for i in a:
# #     print(i**2)
# def largest():
#     return max(a)
# def smallest():
#     return min(a)
# print(smallest())

# a=[1,3,4,"bahavn"]
# b=tuple(a)
# print(b)
# c=("r33bycb",3,9)
# d=list(c)
# print(d)

#a={
#     "bhavan":98,
#     "adarsh":100,
#     "maneesh":100
# }
# b=a.values()
# print(sum(b)/len(b))

# from collections import Counter
# a = "bhavan"
# b = Counter(a)
# print(b)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a|b) #union
# print(a&b) #intersection
# print(a-b)  #difference

# a=[1,1,1,2,3,4,4,5]
# b=set(a)
# print(b) #removes duplicate values

# def is_prime(n):
#     if n<=0:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# n=int(input("enter the number:"))

# if is_prime(n):
#     print("Entered Number is a prime Number")
# else:
#     print("Entered Number is not prime Number")
# n=int(input("enter the number:"))
# i=0
# while i<=10:
#     print(f"{n}x{i}={n*i}")
#     i+=1

# n=10
# a,b=0,1
# for i in range(n):
#     print(a)
#     a,b=b,a+b

