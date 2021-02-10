# these values are not correct, because we don't had access to Google.
# 1 pennie = 1 cent
# 1 nickle = 10 cent
# 1 dime = 20 cent
# 1 quarter = 25 cent
# 1 loonie = 100 cent
# 1 toonie = 200 cent

def solve(number):
    coins = {"toonie": 200, "loonie": 100, "quarter": 25,  "dime": 20, "nickle": 10, "pennie": 1}

    while number > 0:
        for i in coins: 
            if(number >= coins[i]):
                number -= coins[i]
                print(i)
                break
        
solve(int(input("Enter A value to change to coins: ")))