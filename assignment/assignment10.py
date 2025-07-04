
#1.
# class car():
#     def __init__(self,brand,color,year):
#         self.brand=brand
#         self.color=color
#         self.year=year
#     def turnon(self):
#         print("the car has started")
#     def turnoff(self):
#         print("the cas has switched off")
# b=car("toyota","black",2025)
# print(b.turnon())

# class fan():
#     def __init__(self,brand,color,speed):
#         self.brand=brand
#         self.color=color
#         self.speed=speed
#     def turnon(self):
#         print("the fan started roattaing")
#     def turnoff(self):
#         print("the fan has switched off")
# b=fan("toyota","black",2025)
# print(b.turnon())
# print(b.turnoff())

# class tv():
#     def __init__(self,brand,color,year):
#         self.brand=brand
#         self.color=color
#         self.year=year
#     def turnon(self):
#         print("the tv has started")
#     def turnoff(self):
#         print("the tv  has switched off")
# b=tv("samsung","black",2025)
# print(b.turnon())
# print(b.turnoff())

#2.
# class car():
#     def __init__(self,brand,speed,fuel_type):
#         self.brand=brand
#         self.speed=speed
#         self.fuel_type=fuel_type
#     def accelerate(self):
#         print("the car has accelerated")
#     def stop(self):
#         print("the car has switched off")
#     def honk(self):
#         print("it started honking")
# a=car("toyota","black",2025)
# print(a.accelerate())
# print(a.honk())
# print(a.stop())

# class bike():
#     def __init__(self,brand,speed,fuel_type):
#         self.brand=brand
#         self.speed=speed
#         self.fuel_type=fuel_type
#     def accelerate(self):
#         print("the bike has accelerated")
#     def stop(self):
#         print("the bike has switched off")
#     def honk(self):
#         print("it started honking")
# b=bike("toyota","black",2025)
# print(b.accelerate())
# print(b.honk())
# print(b.stop())

# class truck():
#     def __init__(self,brand,speed,fuel_type):
#         self.brand=brand
#         self.speed=speed
#         self.fuel_type=fuel_type
#     def accelerate(self):
#         print("the truck has accelerated")
#     def stop(self):
#         print("the truck has switched off")
#     def honk(self):
#         print("it started honking")
# c=truck("toyota","black",2025)
# print(c.accelerate())
# print(c.honk())
# print(c.stop())


#3.
# class Student():
#     def __init__(self,name,age,height):
#         self.name=name
#         self.age=age
#         self.height=height
#     def passed(self):
#         print(f"{self.name} has passed the exam")
#     def fail(self):
#         print(f"{self.name} has failed in the exam")
# a=Student("bhavan",19,5.11)
# print(a.height)
# print(a.passed())

# class Teacher():
#     def __init__(self,id,name,experience):
#         self.id=id
#         self.name=name
#         self.experience=experience
#     def teaching(self):
#         print(f"{self.name} has started teaching the class")
#     def exp(self):
#         print(f"{self.name} has {self.experience}yrs of experience ")
# b=Teacher(1,"chaitanya",20)
# print(b.name)
# print(b.exp())

# class classroom():
#     def __init__(self,num,floor):
#         self.num=num
#         self.floor=floor
#     def tenth_class(self):
#         print(f"tenth class room is in {self.floor} floor room no-{self.num}")
# b=classroom(2,4)
# print(b.tenth_class())   
# print(b.floor)

#4.
      
# class Products():
#     def __init__(self,name,type_,price):
#         self.name=name
#         self.type_=type_
#         self.price=price
#     def details(self):
#         print(f"the name of the product is {self.name}")
#         print(f"the brand of the product is {self.type_}")
#         print(f"the price of the product is {self.price}")
#     def exp(self):
#         if self.price>100000:
#             print("it is expensive")
#         else:
#             print("affordable")
# a=Products("phone","samsung",120000)
# print(a.price)
# a.exp()
# print(a.details())

# class cart():
#     def __init__(self):
#         self.cart_product=[]
#     def add_products(self,product):
#         self.product=product
#         self.cart_product.append(product)
#         print(f"the product added in cart is {product}")

#     def products_in_cart(self):
#         print(f"the prosudct in the cart is {self.cart_product}")
# b=cart()
# print(b.cart_product)
# b.add_products("Tv")
# b.add_products("laptop")
# print(b.cart_product)

# class user():
#     def __init__(self,id,mail):
#         self.id=id
#         self.mail=mail
#         self.cart=cart()
#     def browse(self):
#         print("browsing the produsts online")
#     def add_to_cart(self,interested_product):
#         self.interested_product=interested_product
#         self.cart.add_products(interested_product)
# c=user(143,"abdc@gmail.com")
# print(c.id)
# c.add_to_cart("fridge")
# print(b.cart_product)
# print(c.cart.cart_product)


#5.

# class book():
#     def __init__(self,author,title):
#         self.author=author
#         self.title=title
#         self.issued=False
#     def issue(self):
#         print("the book has been issued to the student")
#         self.issued=True
#     def read(self):
#         print("student read the book")
#     def returned(self):
#         if self.issued:
#             print("student has returned book")
#         else:
#             print("book has not been issued")

# a=book("ramanujan","wings of fire")
# print(a.title)
# print(a.issue())
# print(a.read())
# print(a.returned())

# class librarian():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     def arrange(self):
#         print("he has arranged the books properly")
#     def update(self):
#         print(f"{self.name} has updated the book records")
# a=librarian("mabbu",143)
# print(a.id)
# print(a.update())

# class Member():
#     def __init__(self,mem_id,end_date,access):
#         self.mem_id=mem_id
#         self.end_date=end_date
#         self.access=access
#     def expire(self):
#         print(f"your membership will be expired on {self.end_date}")
#     def access_to(self):
#         print(f"you have access to {self.access} books")
# a=Member(143,"25-12-25","all")
# print(a.access_to())
# print(a.end_date)


#a=["cat","dog","monkey","cow"]
# for i,animals in enumerate(a):
#     b=animals
#     c=a[(i+1)%len(a)]
#     print(b+c[:2])
    


