#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot Barista!!

print("\nHello, welcome to NetworkJohn Coffee!!!!!!!\n")

name = input("What is your name?\n\n")

print("\nHello " + name + ", thank you so much for coming in today!!\n\nHere is a menu " + name + ".\n")

menu = "Black Coffee, Espresso, Latte, Cappucino"

print("\n" + menu)

order = input()

price = 8

quantity = input("\nHow many " + menu + " would you like?\n")

total = price * int(quantity)

print("Okay " + name + ", your total is $" + str(total) + " dollars.\n\nWe will have that " + str(quantity) + " " + order + " out for you shortly.")
