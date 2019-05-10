string = input("String: ") # <>={}
num = 0
lower = 0
upper = 0
other = 0
lower_com = ["á", "é", "í","ó", "ö", "ő", "ú", "ü", "ű"]
upper_com = ["Á", "É", "Í", "Ó", "Ö", "Ő", "Ú", "Ü", "Ű"]
for i in string.replace(" ", ""):
    if "a" <= i <= "z" or i in lower_com:
        lower += 1
    elif "A" <= i <= "Z" or i in upper_com:
        upper += 1
    elif "0" <= i <= "9":
        num += 1
    else:
        other += 1
print("num = {} lower = {} upper = {} other = {}".format(num, lower, upper, other))
