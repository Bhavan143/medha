
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
        