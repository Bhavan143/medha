
#1.
# class TV:
#     def __init__(self,brand):
#         self.brand=brand
#     def turn_on(self):
#         print("turning on")
#     def turn_off(self):
#         print("turning off")
        
# tv=TV("samsung") 

# class Remote:
#     def __init__(self):
#         self.tv=tv

# remote=Remote()
# print(tv.brand)
# remote.tv.turn_on()
# remote.tv.turn_off()

#2.
# class Engine:
#     def __init__(self):
#         self.car=None
#     def start(self):
#         print(f"{self.car.brand} engine has been started")
#     def stop(self):
#         print("th eengine has been stoped")
# class Car:
#     def __init__(self,brand,engine):
#         self.brand=brand
#         self.engine=engine
#         engine.car=self

# engine=Engine()    
# car=Car("toyota",engine)
# car.engine.start()
        

#3.

# class Light:
#     def __init__(self):
#         pass
#     def switch_on(self):
#         print("the light is on")
#     def switch_off(self):
#         print("the light is off")

# class Room:
#     def __init__(self,light):
#         self.light=light

# light=Light()    
# room=Room(light)
# room.light.switch_on()
# room.light.switch_off()

#4.
# class Laptop:
#     def __init__(self,battery):
#         self.battery=battery

# class Battery:
#     def __init__(self):
#         pass
#     def check_charge(self):
#         print("your charge is 69% now")

# battery=Battery()   
# laptop=Laptop(battery)
# laptop.battery.check_charge()

#5.
# class Mobile:
#     def __init__(self,camera):
#         self.camera=camera
        
# class Camera:
#     def __init__(self):
#         pass
#     def click_pic(self):
#         print("picture is clicked")
# camera=Camera()
# mobile=Mobile(camera)
# mobile.camera.click_pic()
        


# class student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def display_info(self):
#         print(f"{self.name} is of {self.age}yrs and he's grade is {self.grade}")
# student1=student("bhavan",19,"A")
# student1.display_info()
        
# class Bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"the amount of {amount}rs has been deposited the current balance is {self.balance}")
#     def withdraw(self,amount):
#         if amount<self.balance:
#             self.balance-=amount
#             print(f"the amount withdrawn was {amount} and balance left is {self.balance}")
#         else:
#             print("insufficient balance")
#     def show_balance(self):
#         print(f"the present balance is {self.balance}")

  
# bank=Bankaccount(2000000)
# bank.deposit(100)
# bank.show_balance()
# bank.withdraw(1000000)
# bank.show_balance()

# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def read(self):
#         print(f"reading {self.title} by {self.author}")
# book=Book("Wings Of Fire","APJ ADBUL KALAM")
# book.read()
        

# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         self.Area=self.length*self.breadth
#         print(f"the area of rectangle is {self.length}*{self.breadth}={self.Area}")
#     def perimeter(self):
#         self.p=2*(self.length+self.breadth)
#         print(f"the perimeter of rectangle is {self.p}")
# box=rectangle(20,10)
# print(box.length)
# box.area()
# box.perimeter()

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         pi=3.14
#         self.Area=pi*self.radius**2
#         print(f"the area of circle with radius:{self.radius} is : {self.Area}")
# c=Circle(6)
# c.area() 
# print(c.radius)      

# class laptop:
#     def __init__(self,brand,price,RAM):
#         self.brand=brand
#         self.price=price
#         self.RAM=RAM
#     def details(self):
#         print(f"the brand of the laptop is {self.brand}")
#         print(f"the price of the laptop is Rs.{self.price}")
#         print(f"the Ram of the laptop is {self.RAM}")
# laptop1=laptop("lenovo",100000,"12GB")
# laptop2=laptop("DELL",109000,"8GB")  
# laptop3=laptop("ASUS",200000,"16GB") 
# laptop1.details()
# laptop2.details()
# laptop3.details()
