original_price = 3.49
discount = 60/100
user_input = int(input("Amount of loaves for day-old bread: "))
regular_price = original_price*user_input
day_old_bread_price = regular_price*discount
print(f"Regular Price: {regular_price:.2f}\nDiscount: {discount*100:.02f}%\nTotal: {day_old_bread_price:.2f}")
