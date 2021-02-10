while True:
    oneltr_bootles = int(input("Enter the num of 1ltr bottles:"))
    moreltr_bootles = int(input("Enter the num of more than 1ltr bottles: "))
    if(oneltr_bootles == 0 or moreltr_bootles == 0):
        break
    if oneltr_bootles or moreltr_bootles:
        print("Deposit of 1ltr bottles: ",oneltr_bootles * 0.10, "$")
        print(f"Deposit of {moreltr_bootles}ltr bootles: ", moreltr_bootles * 0.25, "$")