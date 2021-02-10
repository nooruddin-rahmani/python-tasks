
foods = ["Rice", "bla", "blabla"]
prices = [10, 12, 22]


tax = [10/100, 12/100, 22/100]
tip = [18/100, 22/100, 30/100]

print("Which one do you want to pick?")
for i in foods: 
    print(i)

user_input = input("\nChoose: ")

if user_input in foods:
    index = foods.index(user_input)
    print("price: $", prices[index], sep="")
    print("tax: $",tax[index], sep="")
    print("tip: $", tip[index], sep="")
    print("total: $", (prices[index]+tax[index]+tip[index]), sep="")

else: 
    print("not available")

