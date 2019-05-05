string = input("String: ") # <>={}
num = 0
lower = 0
upper = 0
other = 0
for i in string:
    if "a" <= i <= "z":
        lower += 1
    elif "A" <= i <= "Z":
        upper += 1
    elif "0" <= i <= "9":
        num += 1
    else:
        other += 1
print("num = {} lower = {} upper = {} other = {}".format(num, lower, upper, other))
