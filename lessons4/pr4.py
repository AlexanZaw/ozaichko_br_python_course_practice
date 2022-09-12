# task 4

piramide_height = int(input("Plaese input the height of the pyramid: "))

i = 1
while i != piramide_height * 2:
    if i > piramide_height and i < piramide_height * 2:
        print("+"*((piramide_height * 2) - i))
    else:
        print("+"*i)
    i += 1
