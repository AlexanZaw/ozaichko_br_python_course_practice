# task3

input_str = input("Please input string: ")

new_str = input_str.split(" ")

i = len(new_str) - 1
result = ""

while i >= 0:
    result += new_str[i]+" "
    i -= 1

print(input_str)
print(result)
