#1.
# def maximum(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# num=maximum(1,2,3)
# print(f"the maximum number is {num}")
# if num>0:
#     print(f"{num} is a positive number")
#     if num%2==0:
#         print(f"{num} is a even number")
#     else:
#         print(f"{num} is a odd number")
# else:
#     print("it is a negative number")


#2.
# a="B"
# v="aeiou"
# for i in a:
#     if i.islower() and i in v:
#         print("it is lower case vowel")
#     elif i.isupper() and i in v:
#         print("it is upper case vowel")  
#     if i.islower() and i not in v:
#         print("it is lower case consonent")
#     elif i.isupper() and i not in v:
#         print("it is upper case consonent") 
#     elif i.isdigit():
#         print("it is a digit")
#     else:
#         print("it is a special character")
        


#3.
# rows=int(input("enter the number of rows:"))
# for i in range(1,rows+1):
#     print(" "*(rows-i)+"*"*(2*i-1))

#4.
# n=int(input("enter the number"))
# def even_(n):
#         if n==0:
#             return 0
#         if n%2==0:
#             print(n,end=" ")
#         even_(n-1)
# print(even_(n))
        

#5.
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
# print(f"distance:{((x**2)+(y**2))**0.5}")

#6.
# n=int(input("enter the number:"))
# def add(n):
#     if n==0:
#         return 0
#     else:
#         return n+ add(n-1)
# print(add(n))

#7.
# def palindrome(n):
#     a=n
#     b=a[::-1]
#     if a==b:
#         return True
#print(palindrome("1221"))
# def anagram(a,b):
#     for i in range(len(a)):
#         word1=[]
#         word1.append(i)
#         word1.sort()
#     for j in range(len(b)):
#         word2=[]
#         word2.append(i)
#         word2.sort()
#     if word1==word2:
#         print("it is an anagram")
#     else:
#         print("not an anagram")   
# anagram("bhavan","navhyb")


# keys = ["name", "age", "occupation"]
# values = ["Emma", 28, "Engineer"]
# person = dict(zip(keys, values))
# print(person)



# nums=[2,5,9,8,10,12,342,344,67]
# def even(nums,i):
#     if i>=len(nums) :
#         return
#     if nums[i]%2==0:
#         print(nums[i],end=" ")
#     even(nums,i+1)
# even(nums,0)
    