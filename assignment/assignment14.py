
# a="'H3ll0_Wor!ld#2025"
# b=""
# for i in a:
#     if i.isalpha():
#         b+=str(i)
# print(type(b))
# print(b)


# from collections import Counter
# a="cat dog dog bird cat cat"
# b=a.split()
# freq=Counter(b)  
# print(freq)
# words_freq=list(freq)
# print(words_freq)


# a = 'crypt'
# vowels = 'aeiou'
# index = -1  
# for i, char in enumerate(a):
#     if char in vowels:
#         index = i
#         break
# print(index)

# a = 'crypet'
# vowels = 'aeiou'
# found = -1

# for i, ch in enumerate(a):
#     if ch in vowels:
#         found = i
#         break

# print(found)



# a='education' 
# vowels="aeiou"
# b=list(a)
# print(b)
# for i in b:
#     if i in vowels:
#         b.remove(i)
#         b.append(i)
# print(b)


# a='education'
# vowels="aeiou"
# b=""
# c=""
# for i in a:
#     if i in vowels:
#         c+=i
#     else:
#         b+=i
# print(b+c)

# from collections import Counter
# a="banana"
# b=dict(Counter(a))
# print(b)


# a="hello world"
# vowels="aeiou"
# for i in vowels:
#     a=a.replace(i,i.upper())
# print(a)


# a = '12345'
# b = list(a)
# c = sorted(b)       
# if b == c:
#     print("True")
# else:
#     print("False")



# a='This is a beautiful sunny day'
# b=a.split()
# result=0
# for i in b:
#     if len(i)>4:
#         result+=1
# print(result)

# a="mysecretpassword1234"
# output="****************yyyy"
# b=a[-4:]
# c=output.replace("yyyy",b)
# print(c)


# a="python"
# for i,char in enumerate(a):
#     print(" "*i+char)
    
# a='open ai builds tools'
# b=a.split()
# print(" ".join(b[::-1]))    

# a="a1b2c3"
# b=list(a)
# for i in b:
#     if i.isdigit():
#         b.remove(i)
# print("".join(b))

# a=[32,45,99,100,122,32]
# def even(a,i):
#     if i>= len(a):
#         return
#     else:
#         if a[i]%2==0:
#             print(a[i])
#     print(even(a,i+1))
# even(a,0)


# import math
# C=40
# H=20
# D=input("enter comma-seperated input:").split(",")
# for i in D:
#     Q = math.sqrt((4 * C * int(i))/H)
#     print(round(Q))




