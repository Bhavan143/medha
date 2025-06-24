
#1.what you want to achieve?
 ##total bill
#2.what u  need to achieve this
 ##dishes and prices
 ##what user wants
 ##how many user wants
#3.arrange the order
 ##dishes and prices
 ##what user wants
 ##how many user wants
 ##total bill
#4.write the code
total_bill=0
menu={
    "dosa":40,
    "idli":35,
    "vada":50,
    "poori":40,
    "upma":30,
}
dish_one_choice=input("what do you wnat?")
dish_one_quantity=int(input("enter how many?"))
dish_two_choice=input("what do you wnat?")
dish_two_quantity=int(input("enter how many?"))
dish_one_bill=(menu.get(dish_one_choice)*(dish_one_quantity))
dish_two_bill=(menu.get(dish_two_choice)*(dish_two_quantity))
a=dish_one_bill+dish_two_bill
gst=(5*a)/100
total_bill=a+gst

detailed=f""""

{dish_one_choice} X {dish_one_quantity}={dish_one_bill}
{dish_two_choice} X {dish_two_quantity}={dish_two_bill}
total_bill_withoutgst={a}
----------------------------------------------------------------------
gst=5%
total_bill={total_bill}


"""
print(detailed)

