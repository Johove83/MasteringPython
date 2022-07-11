#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot Barista!!

print("\nHello, welcome to NetworkJohn Coffee!!!!!!!\n")

name = input("What is your name?\n\n")

print("\nHello " + name + ", thank you so much for coming in today!!\n\nHere is a menu " + name + ".\n")

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

print("\n" + menu)

order = input()
price = 0
if order == "Frappuccino":
    price = 13
    quantity = input("How many " + order + " would you like, " + name + "?\n\n")
    total = price * int(quantity)
    print("Okay " + name + ", your total is $" + str(total) + " dollars.\n\nWe will have that " + str(quantity) + " " + order + " out for you shortly.")
elif order == "Black Coffee":
    price = 3
    quantity = input("How many " + order + " would you like, " + name + "?\n\n")
    total = price * int(quantity)
    print("Okay " + name + ", your total is $" + str(total) + " dollars.\n\nWe will have that " + str(quantity) + " " + order + " out for you shortly.")
elif order == "Espresso":
    price = 5
    quantity = input("How many " + order + " would you like, " + name + "?\n\n")
    total = price * int(quantity)
    print("Okay " + name + ", your total is $" + str(total) + " dollars.\n\nWe will have that " + str(quantity) + " " + order + " out for you shortly.")
elif order == "Latte":
    quantity = input("How many " + order + " would you like, " + name + "?\n\n")
    cream = input("\nWould you like whipped cream with that Latte, " + name + "?\n\n")
    if cream == "Yes":
        price = 11
        total = price * int(quantity)
        print("Okay " + name + ", your total is $" + str(total) + " dollars.\n\nWe will have that " + str(quantity) + " " + order + " out for you shortly.")
    else:
        price = 9
        total = price * int(quantity)
        print("Okay " + name + ", your total is $" + str(total) + " dollars.\n\nWe will have that " + str(quantity) + " " + order + " out for you shortly.")
elif price == "Cappucino":
    price = 10
    quantity = input("How many " + order + " would you like, " + name + "?\n\n")
    total = price * int(quantity)
    print("Okay " + name + ", your total is $" + str(total) + " dollars.\n\nWe will have that " + str(quantity) + " " + order + " out for you shortly.")
else:
    print("Sorry, that is not on our menu.")


    


