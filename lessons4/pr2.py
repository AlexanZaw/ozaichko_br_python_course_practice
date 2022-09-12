# tsask 2

input_str = input("Please input string: ").lower()
input_separator = input("Please input separator: ").lower()

while len(input_str) == 0 or input_separator == '' or input_separator == ' ':
    input_str = input("Please input string: ").lower()
    input_separator = input("Please input separator: ").lower()

result = ""

for ch in input_str:
    if result.find(ch) == -1:
        result += ch+input_separator+str(input_str.count(ch))+", "
    elif ch.isdigit() and result.find(input_separator+ch) != -1:
        result += ch+input_separator+str(input_str.count(ch))+", "



result = result[:-2]
print(result)
