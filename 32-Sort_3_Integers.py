
def sort(i1, i2, i3):
    smallest = min(i1, i2, i3)
    largest = max(i1, i2, i3)

    middle = (i1 + i2 + i3 ) - smallest - largest

    print(smallest, middle, largest)



sort(int(input("i1: ")), int(input("i2: ")), int(input("i3: ")))
