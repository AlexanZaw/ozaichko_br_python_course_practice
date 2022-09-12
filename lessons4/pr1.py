# task1
input_str = input("Please input string; ")

while not input_str.isdigit():
    input_str = input("This tape contains more than just numbers. Please input string: ")

s = 0
for number in input_str:
    s += int(number)

print(f"Summ = {s}")
